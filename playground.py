def fungsi_luar(fungsi_lain):
    def fungsi_dalam():
        print("sebelum fungsi asli")
        fungsi_lain()
        print("sesudah fungsi asli")
    return fungsi_dalam
@fungsi_luar
def salam():
    print("selamat pagi")


salam()

