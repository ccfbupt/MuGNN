import os
import sys
import config
from models import TransE
from project_path import bin_dir

def train(gpu, data_dir):
    os.environ['CUDA_VISIBLE_DEVICES'] = str(gpu)
    con = config.Config()
    con.set_in_path(data_dir)
    con.set_work_threads(8)
    con.set_train_times(1000)
    con.set_nbatches(100)
    con.set_alpha(0.001)
    con.set_bern(0)
    con.set_dimension(100)
    con.set_margin(1.0)
    con.set_ent_neg_rate(1)
    con.set_rel_neg_rate(0)
    con.set_opt_method("SGD")
    con.set_save_steps(10)
    con.set_valid_steps(10)
    con.set_early_stopping_patience(10)
    con.set_checkpoint_dir(data_dir / "checkpoint")
    con.set_result_dir(data_dir / "result")
    # set test to false
    con.set_test_link(False)
    con.set_test_triple(False)
    con.init()
    con.set_train_model(TransE)
    con.train()

def main():
    gpu = sys.argv[1]
    language = sys.argv[2]
    # print(gpu, bin_dir / language)
    train(gpu, bin_dir / language)

if __name__ == '__main__':
    main()