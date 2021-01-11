var mini = true;

function toggleSidebar() {
  if (mini) {
    document.getElementById("mySidebar").style.width = "340px";
    document.getElementById("main").style.marginLeft = "340px";
    this.mini = false;
  } else {
    document.getElementById("mySidebar").style.width = "65px";
    document.getElementById("main").style.marginLeft = "65px";
    this.mini = true;
  }
}
