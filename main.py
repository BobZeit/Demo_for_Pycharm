from Calculate import calculate


def main():
    flag = calculate.get_value()
    if flag:
        a,b,c = flag
        cal = calculate(a,b,c)
        result = cal.calculate_root()
        cal.show_results(result)



if __name__ == "__main__":
    main()
