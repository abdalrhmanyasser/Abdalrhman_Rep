c_path = r"C:\Users\abdal\Desktop\Abdalrhman Yasser\Visual Code\Python\text.jk"
class func:
    def __init__(self, _funcName, _params, _returnType, _placeInFile, _code):
        self.funcName = _funcName
        self.params = _params
        self.returnType = _returnType
        self.placeInFile = _placeInFile
        self.code = _code
    def hello(self):
        print(self.funcName, self.params, self.returnType, self.placeInFile)
try:
    file = open(c_path, "rt")
except:
    file = open(c_path, "x")
    file.close()
    file = open(c_path, "rt")

depth = 0
state = "normal"
var_types = ["int", "string"]
var = {}

def complete_expression(expression_keys):
    sum = 0
    expression_state = "+"
    for i in expression_keys:
        if type(i) == int: 
            if expression_state == "+":
                sum+=int(i)
            elif expression_state == "-":
                sum-=int(i)
            elif expression_state == "*":
                sum*=int(i)
            elif expression_state == "/":
                sum/=int(i)
        if i == "+":
            expression_state = "+"
        elif i == "-":
            expression_state = "-"
        elif i == "*":
            expression_state = "*"
        elif i == "/":
            expression_state = "/"
    return sum
def checkParse(keys, curentLine):
    string="f"
    final_string = ""
    for key in keys:
        if key != "print" and string == "f":
            if key in var:
                return var.get(key)
            if "i" in key:
                return int(key[:-1])
            if "thing" in key:
                return int(key[-1])
        elif "Str" in curentLine:
                for i in curentLine:
                    if i =='"' and string == "t":
                        string = "f"
                        continue
                    if i =='"' and string == "f":
                        string = "t"
                        continue
                    if string == "t":
                        final_string+=i
                        
                
                return final_string
def translate_compute(computekeys):
    computestate = "none"
    for key in computekeys:
        if key in var:
            computekeys[computekeys.index(key)] = var.get(key)
        elif "i" in key:
            computekeys[computekeys.index(key)] = int(key[:-1])
    
    return complete_expression(computekeys)
def parse(depth):
    code = file.read()
    code = code.split("\n")
    line_index = 1
    for cur_line in code:
        keys = cur_line.split(" ")
        if "print" in keys[0]:
            print(checkParse(keys, cur_line))
        elif "func" == keys[0]:
            function_decoded = " ".join(keys[2:]).split("{")
            params = " ".join(function_decoded[1:]).split(", ")
            params = "\\".join(params).split("\\")
            funsc = func(function_decoded[0], params[:-1], keys[1], line_index, code)
            funsc.hello()
        elif "\\" == keys[0]:
            pass
        else:
            if keys[0] not in var:
                if keys[1] == "=":
                    var[keys[0]] = translate_compute(keys[2:])
            else:
                for key in keys[2:]:
                    if key in var:
                        keys[keys.index(key)] = var.get(key)
                    elif "i" in key:
                        keys[keys.index(key)] = int(key[:-1])
                if keys[1] == "+=":
                    var[keys[0]] = var.get(keys[0]) + keys[2]
        line_index+=1
parse(0)
print("#//////////Code Finished//////////#")
print(var)
