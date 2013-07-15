import os, glob

projectPath = os.path.split(os.path.split(os.path.realpath(__file__))[0])[0]
spamPath = os.path.join(projectPath,'data\\spam')
hamPath = os.path.join(projectPath,'data\\ham')
def split_data(test_current, test_total):
  spamFiles = [a for a in glob.glob(spamPath +'\\*.txt')]
  dataset_size = len(spamFiles)//test_total
  test_data = spamFiles[(test_current-1)*dataset_size:test_current*dataset_size]
  spamFiles = [a for a in spamFiles if a not in test_data]
  return (spamFiles,test_data)

print(split_data(1,5))