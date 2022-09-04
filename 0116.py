while True:
    account = int(input('Enter account number: (-1 to end): '))
    if account == -1:
        break
    bigingBalance = float(input('enter biging blance: '))
    totalCharge = float(input('Enter totall charge: '))
    totalCredits = float(input('Enter total credits: '))
    creditslLimit = float(input('Enter credits limt: '))
    if (bigingBalance+totalCharge-totalCredits) > creditslLimit:
        print('Account: {0}'.format(account))
        print('Credits limit: {0}'.format(creditslLimit))
        print('Lance: {0}'.format(bigingBalance+totalCharge-totalCredits))
        print('Credit limited Exceected')