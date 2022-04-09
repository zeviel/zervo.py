# zervo.py
Mobile-API for zervo anime roleplay social network
![](https://play-lh.googleusercontent.com/pFCzgkJqMZebR-0l3dQAC81dLfUCOj8Xy0X97382LMADkrgqgvFzaLDsjIbyc56dXQ)

## Example
```python3
# Simple login with google
import zervo
zervoclient = zervo.ZervoClient()
zervoclient.google_auth(google_id="")
print(f"-- Account user_id is::: {zervoclient.user_id}")
```
