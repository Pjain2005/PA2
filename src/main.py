import sys
from cache import parse_input, fifo_misses, lru_misses


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: python src/main.py <input_file>")
        return 2

    k, _, req = parse_input(sys.argv[1])
    fifo = fifo_misses(k, req)
    lru = lru_misses(k, req)

    print(f"FIFO : {fifo}")
    print(f"LRU : {lru}")
    #OPTFF will be added later

    return 0


if __name__ == "__main__":
    raise SystemExit(main())