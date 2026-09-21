class Solution:
    def numUniqueEmails(self, emails: list[str]) -> int:
        validEmails = []
        count = 0
        for email in emails:
            localName = ""
            domainName = ""
            flag = False
            for i, ch in enumerate(email):
                if "@" not in localName:
                    if flag == True and ch != "@":
                        continue

                    if ch == ".":
                        continue

                    elif ch == "+" and email[i+1] != "@" and i + 1 < len(email):
                        flag = True
                        continue

                    localName += ch

                else:
                    domainName += ch

                finalEmail = localName+domainName
            
            if finalEmail not in validEmails:
                validEmails.append(finalEmail)
                count += 1
        return count