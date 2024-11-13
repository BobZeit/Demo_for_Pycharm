from Calculate import Calculate


def main():
    flag = Calculate.get_value()
    if flag:
        a,b,c = flag
        cal = Calculate(a, b, c)
        result = cal.calculate_root()
        cal.show_results(result)



if __name__ == "__main__":
    main()
