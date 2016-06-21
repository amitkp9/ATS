
from models.ats_model import ATSModel

if __name__ == "__main__":
    model = ATS(host='localhost',
                     port=7496,
                     client_id=101,
                     is_use_gateway=False,
                     evaluation_time_secs=20,
                     resample_interval_secs='30s')
    model.start(["JPM", "C"], 100)