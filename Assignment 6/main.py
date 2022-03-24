import constants
import func_lib as fl


fl.sendKeys(fl.findElement("email"), constants.username)
fl.sendKeys(fl.findElement("pass"), constants.password)
fl.click(fl.findElement("login"))
