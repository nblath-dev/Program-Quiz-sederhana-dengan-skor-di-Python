import sys,time

# JANGAN MENYALAH GUNAKAN PROGRAM INI
# PROGRAM INI DIBUAT HANYA UNTUK PEMBELAJARAN
# DAN SEMOGA KALIAN BISA MENJADI MANUSIA YANG BERMAANFAAT UNTUK MASYARAKAT
# AMIN :)


nilai_benar = 0
nilai_salah = 0

def ketik(teks):
    for i in teks + "\n":
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.1)


time.sleep(0.2)
print("██   ████")
time.sleep(0.2)
print("█ █     █")
time.sleep(0.2)
print("█  █    █")
time.sleep(0.2)
print("█   █   █")
time.sleep(0.2)
print("██████  █")
time.sleep(0.2)
print("█     █ █")
time.sleep(0.2)
print("█████████")

ketik("\33[36mInstagram :\33[0m \33[32m@nbltpr\33[0m")

print("")
ketik("SELAMAT DATANG DI\nQUIZ PYTHON!!")
print("")
print("Mulai?")
start = input("[TEKAN ENTER UNTUK MULAI] : ")

if start == "":
        # Pertanyaan 1 (Kalian bisa ubah pertanyaan ini)
    print("1.Program ini menggunakan bahasa pemrograman apa?")
    print("")
    print("a.Python\nb.Java\nc.Html\nd.Css")
    print("")
    jawab1 = input("[a/b/c/d] : ")
    print("")
    if jawab1 == "a":
        print("\33[92m\033[1mKamu Benar!\33[0m\33[0m")
        nilai_benar += 1
    else:
        print("\33[31m\033[1mKamu Salah!\33[0m\33[0m")
        print("\33[92mJawaban yang benar adalah a.Python\33[0m")
        nilai_salah += 1


        # Pertanyaan 2 (Kalian bisa ubah pertanyaan ini)
    print("2.Bagaimana cara memunculkan text di python?")
    print("")
    print("a.if else\nb.start\nc.print("")\nd.<p></p>")
    print("")
    jawab1 = input("[a/b/c/d] : ")
    print("")
    if jawab1 == "c":
        print("\33[92m\033[1mKamu Benar!\33[0m\33[0m")
        nilai_benar += 1
    else:
        print("\33[31m\033[1mKamu Salah!\33[0m\33[0m")
        print("\33[92mJawaban yang benar adalah c.print("")\33[0m")
        nilai_salah += 1

        # Pertanyaan 3 (Kalian bisa ubah pertanyaan ini)
    print("3.Program ini menggunakan Python versi berapa?")
    print("")
    print("a.Python 1\nb.Python 2\nc.Python 3\nd.Python 4")
    print("")
    jawab1 = input("[a/b/c/d] : ")
    print("")
    if jawab1 == "c":
        print("\33[92m\033[1mKamu Benar!\33[0m\33[0m")
        nilai_benar += 1
    else:
        print("\33[31m\033[1mKamu Salah!\33[0m\33[0m")
        print("\33[92mJawaban yang benar adalah c.Python 3\33[0m")
        nilai_salah += 1

    print("")
    print("")

    print("\33[92m\033[1mTotal Jawaban Yang Benar : ", nilai_benar, "\33[0m")
    print("\33[31m\033[1mTotal Jawaban Yang Salah", nilai_salah, "\33[0m")
    print("")

    print("JIKA ADA BUG YANG DITEMUKAN, MOHON DM INSTAGRAM @nbltpr")

    
    


else:
    print("")
    print("Baiklah kalau begitu\nMungkin lain kali ya")

