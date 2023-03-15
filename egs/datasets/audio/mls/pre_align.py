import os

from data_gen.tts.vocoder_pre_align import VocoderPreAlign
import tqdm
# import glob


class MLSPreAlign(VocoderPreAlign):
    def meta_data(self):
        # wav_fns = glob.glob(f'{self.raw_data_dir}/wav/audio/*.wav')
        file1 = open('/data/neil/mls/c1_ex1/mlsc1_transcript_all.txt', 'r')
        lines = file1.readlines()
        for line in lines:
            wav_fn, txt, spk = line.split("|")
            # print(wav_fn, txt, spk)
            # exit()
            item_name = os.path.basename(wav_fn)[:-4]
            spk = spk.split("\n")[0]
            # print(item_name, wav_fn, txt, spk)
            # print(os.path.exists(wav_fn))
            if os.path.exists(wav_fn):
                yield item_name, wav_fn, txt, spk


if __name__ == "__main__":
    MLSPreAlign().process()
