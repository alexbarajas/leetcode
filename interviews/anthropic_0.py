

def solution(queries):
    accounts = {}
    results = []
    accounts_with_most_activity = {}
    transfers = 0
    successful_transfers = {}

    TRANSFER_EXPIRATION_PERIOD = 86400000  # 24 hours in milliseconds

    for query in queries:
        if query[0] == "CREATE_ACCOUNT":
            timestamp = query[1]
            account = query[2]
            if account in accounts:
                results.append(False)
            else:
                accounts[account] = {"time_created": timestamp, "balance": 0, "transactions": [], "pending": 0}
                accounts_with_most_activity[account] = 0
                results.append(True)
        elif query[0] == "TOP_ACTIVITY":
            n = int(query[2])
            # Sort by balance first (descending), then by account name (ascending)
            sorted_account_transactions = sorted(accounts_with_most_activity.items(), key=lambda x: (-x[1], x[0]))
            resulting_transactions = []
            for i in range(min(n, len(sorted_account_transactions))):
                account, balance = sorted_account_transactions[i]
                resulting_transactions.append(f"{account}({balance})")
            results.append(", ".join(resulting_transactions))
        elif query[0] == "TRANSFER":
            timestamp = query[1]
            account1 = query[2]
            account2 = query[3]
            amount = query[4]
            if account1 not in accounts or account2 not in accounts or account1 == account2 or accounts[account1]["balance"] < int(amount):
                results.append("")
            else:
                transfers += 1
                transfer_id = f"transfer{transfers}"
                accounts[account1]["balance"] -= int(amount)
                accounts[account2]["pending"] += int(amount)
                successful_transfers[transfer_id] = {"timestamp": timestamp, "source": account1, "target": account2, "amount": amount}
                results.append(transfer_id)
        elif query[0] == "ACCEPT_TRANSFER":
            timestamp = int(query[1])
            account = query[2]
            transfer_id = query[3]
            if transfer_id in successful_transfers:
                transfer = successful_transfers[transfer_id]
                if transfer["target"] != account:
                    results.append(False)
                elif (timestamp - transfer["timestamp"]) >= TRANSFER_EXPIRATION_PERIOD:
                    results.append(False)
                else:
                    accounts[account]["balance"] += transfer["amount"]
                    accounts[account]["pending"] -= transfer["amount"]
                    accounts[transfer["source"]]["transactions"].append((transfer["timestamp"], -transfer["amount"]))
                    accounts[transfer["target"]]["transactions"].append((transfer["timestamp"], transfer["amount"]))
                    accounts_with_most_activity[transfer["source"]] += transfer["amount"]
                    accounts_with_most_activity[transfer["target"]] += transfer["amount"]
                    successful_transfers.pop(transfer_id)
                    results.append(True)
            else:
                results.append(False)
        elif query[0] == "ACCOUNT_MERGE":
            account1 = query[2]
            account2 = query[3]
            if account1 not in accounts or account2 not in accounts:
                results.append(False)
                continue
            accounts[account1]["balance"] += accounts[account2]["balance"]
            accounts[account1]["transactions"].extend(accounts[account2]["transactions"])
            accounts.pop(account2)
            results.append(True)
        else:
            account = query[2]
            amount = query[3]
            if account not in accounts:
                results.append("")
            else:
                if query[0] == "DEPOSIT":
                    accounts[account]["balance"] += int(amount)
                elif query[0] == "PAY":
                    if int(amount) > accounts[account]["balance"]:
                        results.append("")
                        continue
                    accounts[account]["balance"] -= int(amount)
                results.append(str(accounts[account]["balance"]))
                accounts_with_most_activity[account] += int(amount)

    return results


queries1 = [
    ["CREATE_ACCOUNT", 1, "account1"],
    ["CREATE_ACCOUNT", 2, "account2"],
    ["DEPOSIT", 3, "account1", 1000],
    ["DEPOSIT", 4, "account2", 1500],
    ["PAY", 5, "account1", 1000],
    ["PAY", 6, "account2", 2000],
    ["TOP_ACTIVITY", 7, 2],
    ["CREATE_ACCOUNT", 8, "account3"],
    ["CREATE_ACCOUNT", 9, "account4"],
    ["CREATE_ACCOUNT", 10, "account5"],
    ["DEPOSIT", 11, "account3", 2500],
    ["DEPOSIT", 12, "account4", 2500],
    ["DEPOSIT", 13, "account5", 2500],
    ["TOP_ACTIVITY", 14, 2],
    ["TOP_ACTIVITY", 15, 3],
    ["TOP_ACTIVITY", 16, 5],
    ["TRANSFER", 17, "account1", "account3", 500],
    ["TRANSFER", 18, "account2", "account4", 1000],
    ["ACCEPT_TRANSFER", 19, "account3", "transfer1"],
    ["ACCEPT_TRANSFER", 20, "account4", "transfer2"],
    ["ACCEPT_TRANSFER", 21, "account4", "transfer1"],
    ["ACCOUNT_MERGE", 22, "account1", "account2"]
]
result1 = [True, True, '1000', '1500', '0', '', 'account1(2000), account2(1500)', True, True, True, '2500', '2500', '2500', 'account3(2500), account4(2500)', 'account3(2500), account4(2500), account5(2500)', 'account3(2500), account4(2500), account5(2500), account1(2000), account2(1500)', "", "transfer1", False, False, True, True]
print(solution(queries=queries1))
print(solution(queries=queries1) == result1)
