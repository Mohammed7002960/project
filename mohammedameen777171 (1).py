admin_role = "admin"
user_role = "kullanici"
users = {
    "admin": "12345",
    "kullanici": "67890"
}
def show_menu():
    print("1-Sisteme Üye Ol")
    print("2-Sisteme Giriş Yap")
    print("3-Şifremi Unuttum")
def register():
    username = input("Kullanıcı Adı: ")
    password = input("Şifre: ")
    print("Kayıt başarılı.")

def login():
    username = input("Kullanıcı Adı: ")
    password = input("Şifre: ")
    if username in users and users[username] == password:
        print("Giriş başarılı.")
        if username == admin_role:
            admin_actions()
        else:
            user_actions()
    else:
        print("Hatalı kullanıcı adı veya şifre.")

def forgot_password():
    username = input("Kullanıcı Adı: ")
    print("Şifre sıfırlama başarılı.")

def admin_actions():
    print("Admin işlemleri yapılacak.")

def user_actions():
    print("Kullanıcı işlemleri yapılacak.")

while True:
    show_menu()
    choice = input("Bir işlem seçin (1-3): ")
    if choice == "1":
        register()
    elif choice == "2":
        login()
    elif choice == "3":
        forgot_password()
    else:
        print("Geçersiz seçenek. Tekrar deneyin.")

