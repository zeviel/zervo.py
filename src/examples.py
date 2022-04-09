# Login with google
import zervo
zervoclient = zervo.ZervoClient()
zervoclient.google_auth(google_id="")
print(f"-- Account user_id is::: {zervoclient.user_id}")
