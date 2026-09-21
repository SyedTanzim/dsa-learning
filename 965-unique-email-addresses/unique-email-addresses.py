class Solution:
    def numUniqueEmails(self, emails: list[str]) -> int:
        validEmails = set()
        
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
            
            validEmails.add(finalEmail)
        return len(validEmails)