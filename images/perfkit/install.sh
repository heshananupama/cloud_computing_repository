#apt update && apt install -y git
#git clone https://github.com/GoogleCloudPlatform/PerfKitBenchmarker.git
cd PerfKitBenchmarker
#python3 -m pip install -r requirements.txt
#python3 ./pkb.py --benchmarks=iperf,coremark,unixbench --benchmark_config_file=/opt/config.yaml --static_vm_file=/opt/vm.json
python3 ./pkb.py --benchmarks=netperf --benchmark_config_file=/opt/config.yaml --static_vm_file=/opt/vm.json
