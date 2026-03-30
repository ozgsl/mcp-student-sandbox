TAX_RATE = 0.15
DEFAULT_LOG_FILE = "log.txt"


def calculate_total(amount, tax_rate=TAX_RATE):
    return amount * (1 + tax_rate)


def format_total(total):
    return f"Total: {total:.2f}"


def print_totals(totals):
    for total in totals:
        print(format_total(total))


def append_results_to_log(results, log_file=DEFAULT_LOG_FILE):
    with open(log_file, "a", encoding="utf-8") as file:
        file.write(f"{results}\n")


def process_data(data, tax_rate=TAX_RATE, log_file=DEFAULT_LOG_FILE):
    totals = [calculate_total(item, tax_rate) for item in data]
    print_totals(totals)
    append_results_to_log(totals, log_file)
    return totals
