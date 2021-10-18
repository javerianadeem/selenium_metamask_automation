Introduction:
This package is created to automate metamask wallet extension using selenium webdriver. 

To install the package, run:

pip install ./selenium_metamask_automation

Check if package exists:

Now check if the package has been installed successfully using the command below:

pip list

Functions:

To download the extension:

selenium_metamask_automation.downloadMetamaskExtension()

This function has to be run once before all functions to download the metamask extension. If you change the directory or create your python file somewhere else, this needs to be run first otherwise following exception will be thrown:

“Path to extension does not exist”

To launch the extension use the function below

selenium_metamask_automation.launchMetamaskExtension(args)
args: path to chrome webdriver



This function returns a value which contains the driver. You can retrieve it like:

driver = launchSeleniumWebdriver(r‘C:\Drivers\chromedriver_win32\chromedriver.exe’)


Now use can call any selenium method using this driver variable

driver.get("https://google.com")


To import wallet

selenium_metamask_automation.metamaskSetup(arg1, arg2)

arg1 : seed phrase of wallet
arg2: password of wallet


To Change the metamask Network:

selenium_metamask_automation.changeMetamaskNetwork(arg)


arg: network name

The network names are mentioned below. On selecting any other network, it will throw an error.

Ethereum Mainnet
Ropsten Test Network
Kovan Test Network
Rinkeby Test Network
Goerli Test Network


To connect to any website use the function below:

selenium_metamask_automatiom.connectToWebsite()


In order to use this function, you have to visit the website first

driver.get("https://google.com")

selenium_metamask_automatiom.connectToWebsite()

For approval transactions:

Confirm: selenium_metamask_automation.confirmApprovalFromMetamask()

Reject: selenium_metamask_automation.rejectApprovalFromMetamask()


For transactions other than approval:

Confirm: selenium_metamask_automation.confirmTransactionFromMetamask()

Reject: selenium_metamask_automation.rejectTransactionFromMetamask()

To add token in your metamask wallet:

selenium_metamask_automation.addToken(arg)

arg: contract address of token



Sign:

signConfirm: selenium_metamask_automation.signConfirm()

signReject: selenium_metamask_automation.signReject()


Errors you might face:

pip list shows the package “selenium_metamask_automation” but your IDE does not detect the package

Solution:

Go to IDE settings > Python Interpreter 

Change the path to C://ProgramFiles//Python//python.exe or in your case add the path where python.exe is installed
