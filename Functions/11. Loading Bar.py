
def loading_status(loading):
    if loading == 100:
        print(f"100% Complete!")
        print(f"[%%%%%%%%%%]")
    else:
        percent = loading // 10 * "%"
        dots = (10 - (loading // 10)) * "."
        print(f"{loading}% [{percent}{dots}]")
        print("Still loading...")


loading = int(input())
loading_status((loading))