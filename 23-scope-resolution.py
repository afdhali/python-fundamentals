# scope resolution = (LEGB) Local-> Enclosed-> Global-> BuiltIn

# Built-in (B)
len = "ini bukan len biasa"   # ← jangan lakukan ini di kode sungguhan!

x = 100           # Global (G)


def outer():      # ────────────────
    x = 200       # Enclosing (E)

    def inner():
        x = 300   # Local (L)
        print(x)  # 300  ← Local ditemukan duluan

    inner()
    print(x)      # 200  ← Enclosing


outer()
print(x)          # 100  ← Global
