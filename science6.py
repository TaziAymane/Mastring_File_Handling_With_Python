class LoginEvent:
    def __init__(self , user , ip , success):
        self.user = user
        self.ip = ip
        self.success = success
    
    def __str__(self):
        status = "SUCCESS" if self.success else "FAIL"
        return f"User {self.user} from  {self.ip} : {status}"
    def __repr__(self):
        return(
            f"LoginEvent(user={self.user!r},"
            f"ip={self.ip!r},"
            f"success={self.success!r}"
        )
e = LoginEvent("admin", "192.168.1.1", False)
# print(e)
print(e)