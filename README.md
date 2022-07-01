
## Introduction
This package is created to automate metamask wallet extension using selenium webdriver. 

#### To Install The Package:



```sh
pip install ./selenium_metamask_automation
```
or
```sh
pip install -i https://test.pypi.org/simple/ selenium-metamask-automation
```
Check if the package exists
```sh
pip list
```

## Functions

#### 1. To download the extension:

```sh
selenium_metamask_automation.downloadMetamaskExtension()
```
This function has to be run once before all functions to download the metamask extension. If you change the directory or create your python file somewhere else, this needs to be run first otherwise following exception will be thrown:

“Path to extension does not exist”

#### 2. To launch the extension use the function below
```sh
selenium_metamask_automation.launchMetamaskExtension(args)
```
args: path to chrome webdriver



This function returns a value which contains the driver. You can retrieve it like:
```sh
driver = launchSeleniumWebdriver(r‘C:\Drivers\chromedriver_win32\chromedriver.exe’)
```

Now use can call any selenium method using this driver variable
```sh
driver.get("https://google.com")
```
#### 3. To import wallet
```sh
selenium_metamask_automation.metamaskSetup(arg1, arg2)
```
arg1 : seed phrase of wallet
arg2: password of wallet


#### 4. To Change the metamask Network:
```sh
selenium_metamask_automation.changeMetamaskNetwork(arg)
```

arg: network name

The network names are mentioned below. On selecting any other network, it will throw an error.

- Ethereum Mainnet
- Ropsten Test Network
- Kovan Test Network
- Rinkeby Test Network
- Goerli Test Network

#### 4. To connect to any website use the function below:
```sh
selenium_metamask_automation.connectToWebsite()
```

In order to use this function, you have to visit the website first
```sh
driver.get("https://google.com")
selenium_metamask_automatiom.connectToWebsite()
```

#### 6. For approval transactions:

Confirm: 
```sh 
selenium_metamask_automation.confirmApprovalFromMetamask()
```

Reject: 
```sh 
selenium_metamask_automation.rejectApprovalFromMetamask()
```


#### 7. For transactions other than approval:

Confirm: 
```sh
selenium_metamask_automation.confirmTransactionFromMetamask()
```

Reject: 
```sh
selenium_metamask_automation.rejectTransactionFromMetamask()
```

#### 8. To add token in your metamask wallet:

```sh
selenium_metamask_automation.addToken(arg)
```
arg: contract address of token

#### 9. Sign:

signConfirm: 
```sh
selenium_metamask_automation.signConfirm()
```
signReject: 
```sh
selenium_metamask_automation.signReject()
```


### Errors you might face:

pip list shows the package ```“selenium_metamask_automation”``` but your IDE does not detect the package

##### Solution:

Go to IDE settings > Python Interpreter 

Change the path to C://ProgramFiles//Python//python.exe or in your case add the path where python.exe is installed
