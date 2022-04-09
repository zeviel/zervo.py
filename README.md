# zervo.py
Mobile-API for [zervo](https://play.google.com/store/apps/details?id=com.planet.pinponapp) anime roleplay social network
![](https://camo.githubusercontent.com/55363398856946d1ceb8fb881b217a5b2dc67b22cc7fa756b37771750d832684/68747470733a2f2f706c61792d6c682e676f6f676c6575736572636f6e74656e742e636f6d2f7046437a676b4a714d5a6562522d306c33645141433831644c6655434f6a385879305839373338324c4d41446b7267716776467a614c44736a496279633536645851)

## Example
```python3
# Login with google
import zervo
zervoclient = zervo.ZervoClient()
zervoclient.google_auth(google_id="")
print(f"-- Account user_id is::: {zervoclient.user_id}")
```
