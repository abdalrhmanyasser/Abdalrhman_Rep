#include <iostream>
#include <chrono>
#include <vector>
#include <sys/types.h>
#include <string.h>
#include <winsock2.h>
#include <ws2tcpip.h>

#pragma comment(lib, "Ws2_32.lib")
using namespace std;

#define DEFAULT_PORT "11135" // 2306039135 --> 9135 + 2000 = 11135
#define DEFAULT_SERVER "127.0.0.1"
#define BUFFER_SIZE 1024

int main()
{
    WSADATA wsaData;
    int iResult;

    SOCKET ConnectSocket = INVALID_SOCKET;
    struct addrinfo* result = NULL, * ptr = NULL, hints;

    char recvbuf[BUFFER_SIZE];
    int recvbuflen = BUFFER_SIZE;

    // Initialize Winsock
    iResult = WSAStartup(MAKEWORD(2, 2), &wsaData);
    if (iResult != 0) {
        std::cerr << "WSAStartup failed with error: " << iResult << std::endl;
        return -1;
    }

    ZeroMemory(&hints, sizeof(hints));
    hints.ai_family = AF_INET;
    hints.ai_socktype = SOCK_STREAM;
    hints.ai_protocol = IPPROTO_TCP;

    // Resolve the server address and port
    iResult = getaddrinfo(DEFAULT_SERVER, DEFAULT_PORT, &hints, &result);
    if (iResult != 0) {
        std::cerr << "getaddrinfo failed with error: " << iResult << std::endl;
        WSACleanup();
        return -1;
    }
    // Attempt to connect to the first address returned by the call to getaddrinfo
    for (ptr = result; ptr != NULL; ptr = ptr->ai_next) {
        // Create a socket for connecting to the server
        ConnectSocket = socket(ptr->ai_family, ptr->ai_socktype, ptr->ai_protocol);
        if (ConnectSocket == INVALID_SOCKET) {
            std::cerr << "Socket failed with error: " << WSAGetLastError() << std::endl;
            WSACleanup();
            return -1;
        }

        // Connect to the server
        iResult = connect(ConnectSocket, ptr->ai_addr, (int)ptr->ai_addrlen);
        if (iResult == SOCKET_ERROR) {
            closesocket(ConnectSocket);
            ConnectSocket = INVALID_SOCKET;
            continue;
        }
        break;
    }

    freeaddrinfo(result);

    if (ConnectSocket == INVALID_SOCKET) {
        std::cerr << "Unable to connect to server!" << std::endl;
        WSACleanup();
        return -1;
    }
    vector<chrono::microseconds> results;
    auto start = chrono::high_resolution_clock::now(); // set temp time (will be overwritten)
    auto stop = chrono::high_resolution_clock::now(); // set temp time (will be overwritten)
    std::cout << "Connected to server." << std::endl;
    for (int i = 0; i < 10; i++) {
        // Send and receive data
        cout << "Ping #" << i + 1 << " :" << endl;
        const char* sendbuf = "PING";
        auto start = chrono::high_resolution_clock::now();
        iResult = send(ConnectSocket, sendbuf, (int)strlen(sendbuf), 0);
        if (iResult == SOCKET_ERROR) {
            std::cerr << "Send failed with error: " << WSAGetLastError() << std::endl;
            closesocket(ConnectSocket);
            WSACleanup();
            return -1;
        }

        // std::cout << "Bytes sent: " << iResult << std::endl;

        // Receive data from the server
        iResult = recv(ConnectSocket, recvbuf, recvbuflen, 0);
        auto stop = chrono::high_resolution_clock::now();
        if (iResult > 0) {
            // std::cout << "Bytes received: " << iResult << std::endl;
            std::cout << "Server response: " << std::string(recvbuf, iResult) << std::endl;
        }
        else if (iResult == 0) {
            std::cout << "Connection closed by server." << std::endl;
        }
        else {
            std::cerr << "Recv failed with error: " << WSAGetLastError() << std::endl;
        }
        auto duration = chrono::duration_cast<chrono::microseconds>(stop - start);
        results.push_back(duration);
        cout << "Time taken for ping: "
             << duration.count() << " microseconds" << endl << endl;
    }


    char* sendbuf = "QUIT";
    iResult = send(ConnectSocket, sendbuf, (int)strlen(sendbuf), 0);

    long long sum = 0;
    for (int i = 0; i < results.size(); i++){
        sum += results[i].count();
    }
    cout << "the average ping time is : " << sum / results.size() << "us" << endl;

    // Cleanup
    closesocket(ConnectSocket);
    WSACleanup();
    std::cout << "Client shut down." << std::endl;
    
    return 0;
}