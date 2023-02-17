import os
import sys
from subprocess import Popen, PIPE

print("Import works!!")

class MasterEnv():
    
    def __init__(self, exe_file, mapping_file, noc_bw, offchip_bw, l1_size, l2_size, num_pe):
        
        
        self._executable = exe_file
        self.mapping_file = mapping_file
        self.NocBW = noc_bw
        self.offchipBW = offchip_bw
        self.l1_size = l1_size
        self.l2_size = l2_size
        self.num_pe = num_pe
        self._executable = exe_file
    

    def run_maestro(self):

        command = [self._executable,
           "--Mapping_file={}.m".format(self.mapping_file),
           "--full_buffer=false",
           "--noc_bw_cstr={}".format(self.NocBW),
           "--noc_hops=1",
           "--noc_hop_latency=1",
           "--offchip_bw_cstr={}".format(self.offchipBW),
           "--noc_mc_support=true",
           "--num_pes={}".format(int(self.num_pe)),
           "--num_simd_lanes=1",
           "--l1_size_cstr={}".format(self.l1_size),
           "--l2_size_cstr={}".format(self.l2_size),
           "--print_res=false",
           "--print_res_csv_file=true",
           "--print_log_file=false",
           "--print_design_space=false",
           "--msg_print_lv=0"]

        print(command)
        process = Popen(command, stdout=PIPE, stderr=PIPE)
        stdout, stderr = process.communicate()
        process.wait() 
        print(stdout)




if __name__ == "__main__":
        
        exe_file = "../../cost_model/maestro"
        mapping_file = "mapping_file"
        noc_bw = 1073741824
        offchip_bw = 1073741824
        l1_size = 1073741824
        l2_size = 1073741824
        num_pe = 1024
        
        env = MasterEnv(exe_file, mapping_file, noc_bw, offchip_bw, l1_size, l2_size, num_pe)
        env.run_maestro()





  
                