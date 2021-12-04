from qqwry import qqwry

if __name__ == '__main__':

    cz = qqwry()
    print(cz.get_version())

    infile = open("ip.txt")
    outfile = open('result.txt', 'a')

    while 1:
        ip = infile.readline()
        if not ip:
            break
        print('{},{}'.format(ip.replace("\n", ""), cz.get_addr_by_ip(ip)))
        outfile.writelines('{},{}\n'.format(ip.replace("\n", ""), cz.get_addr_by_ip(ip)))

    infile.close()
    outfile.close()
