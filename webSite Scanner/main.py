from general import *
from domain_name import *
from ip_address import *
from nmap import *
from robots_txt import *
from whois import *

ROOT_DIR = 'companies'
create_dir(ROOT_DIR)

def gather_info(name, url):
    domain_name = get_ip_address(url)
    ip_address = get_ip_address(url)
    nmap = get_nmap('-F', ip_address)
    robot_txt = get_robots_txt(url)
    whois = get_whois(domain_name)

    create_report(name, url, domain_name, nmap,robot_txt, whois)

def create_report(name, url, domain_name, nmap,robot_txt, whois):
    project_dir = ROOT_DIR + '/' +name;
    create_dir(project_dir)
    write_file(project_dir + '/full_url.txt', url);
    write_file(project_dir + '/demain_naim.txt', domain_name);
    write_file(project_dir + '/nmap.txt', name);
    write_file(project_dir + '/robots_txt.txt', robot_txt);
    write_file(project_dir + '/whois.txt', whois);


gather_info('thenewboston.com', 'https://www.thenewboston.com')