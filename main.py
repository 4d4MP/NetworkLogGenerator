import yaml
from munch import munchify
from random import randint as r

def get_config():
    #read main.yml
    with open("main.yml", "r") as file:
        cfg = munchify(yaml.load(file, Loader=yaml.FullLoader))

    return cfg

def random_element(l):
    size = len(l)
    return l[r(0, size-1)]

def ip_list_generator(count, use_only_local_ips):
    ip_list = []
    if use_only_local_ips:
        for i in range(count):
            ip = f"192.168.{r(0, 255)}.{r(0, 255)}"
            ip_list.append(ip)
    else:
        for i in range(count):
            ip = f"{r(0, 255)}.{r(0, 255)}.{r(0, 255)}.{r(0, 255)}"
            ip_list.append(ip)
    
    return ip_list

def generate_log_entry(source, target, log_level, port, size):
    return f"Source: {source} -> Target: {target} -- Log level: {log_level} -- Port: {port} -- Packet size: {size}"

def write_to_file(file, log_content):
    with open(file, "w") as f:
        for log in log_content:
            f.write(f"{log}\n")
            
def get_packet_size(min, max):
    return r(min, max)
    

def __main__():
    cfg = get_config()
    use_only_local_ips = cfg.use_only_local_ips
    ip_list = ip_list_generator(cfg.number_of_ips, use_only_local_ips)
    log_level_list = cfg.used_log_levels
    port_list = cfg.used_ports
    minimum_packet_size = cfg.min_packet_size
    maximum_packet_size = cfg.max_packet_size
    output_file = cfg.output_file
    message_count = cfg.total_message_counter
    log_content = []
    for i in range(message_count):
        source = random_element(ip_list)
        target = random_element(ip_list)
        log_level = random_element(log_level_list)
        port = random_element(port_list)
        size = get_packet_size(minimum_packet_size, maximum_packet_size)
        log_content.append(generate_log_entry(source, target, log_level, port, size))
    write_to_file(output_file, log_content)
    
if __name__ == "__main__":
    __main__()