import time
import sys
import importlib
sys.stdout.reconfigure(encoding='utf-8')

def formatTime(start,end):
    delta_us=(end - start)*1000000

    us=int(delta_us % 1000)
    ms=int((delta_us / 1000) % 1000)
    s =int((delta_us / 1000000) % 60)
    m =int((delta_us / 60000000) % 60)
    h =int(delta_us / 3600000000)

    # Goal: always show around 3 digits of accuracy
    if h > 0:
        timer_show=f"{h}h {m}m"
    elif m > 0:
        timer_show=f"{m}m {s}s"
    elif s >= 10:
        timer_show=f"{s}.{ms // 100} s"
    elif s > 0:
        timer_show=f"{s}.{ms:03} s"
    elif ms >= 100:
        timer_show=f"{ms} ms"
    elif ms > 0:
        timer_show=f"{ms}.{us // 100} ms"
    else:
        timer_show=f"{us} µs"

    return timer_show

def readInput(folder):
    with open(folder+'/input.txt') as fp:
        lines = fp.readlines()
    return [l.replace('\n','') for l in lines]

def main() -> int:
    """Specify which problem to run. Takes a single integer argument"""
    if len(sys.argv) <= 1:
        print("Please specify the problem number")
        return 1
    else:
        try:
            lib = f"Day {int(sys.argv[1]):02}.Solution"
            sol = importlib.import_module(lib)
        except ValueError:
            print("Please specify the problem number")
            return 1
        except ModuleNotFoundError:
            print(f"No solution for problem {sys.argv[1]} yet")
            return 1

        # Execution stuff
        lines = readInput(f"Day {int(sys.argv[1]):02}")

        tic = time.perf_counter()
        P1 = sol.Part1(lines)
        toc = time.perf_counter()
        print("Part 1:")
        print("\t" + str(P1))
        print("\t"+formatTime(tic,toc))
        print()

        tic = time.perf_counter()
        P2 = sol.Part2(lines)
        toc = time.perf_counter()
        print("Part 2:")
        print("\t" + str(P2))
        print("\t"+formatTime(tic,toc))
        print()

if __name__ == '__main__':
    sys.exit(main())