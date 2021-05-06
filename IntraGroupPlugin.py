import PyPluMA

class IntraGroupPlugin:
    def input(self, filename):
      # Parameter file
      self.parameters = dict()
      paramfile = open(filename, 'r')
      for line in paramfile:
         contents = line.split('\t')
         self.parameters[contents[0]] = contents[1].strip()

      self.tsvfile = open(PyPluMA.prefix()+"/"+self.parameters["tsvfile"], 'r')
      self.mapfile = open(PyPluMA.prefix()+"/"+self.parameters["mapfile"], 'r')
      self.group = self.parameters["group"]


    def run(self):
        pass

    def output(self, filename):
      outfile = open(filename, 'w')
      header = self.tsvfile.readline().strip().split('\t')


      samples = []
      samples2 = []
      for line in self.mapfile:
         contents = line.strip().split('\t')
         if (contents[3] == self.group):
             samples.append(contents[0])
         #else:#if (contents[3] == self.group2):
         #    samples2.append(contents[0])

      results = []
      for line in self.tsvfile:
         contents = line.strip().split('\t')
         sample = contents[0]
         if (sample in samples):
             contents = contents[1:]
             idx = header.index(sample)
             for i in range(idx+1, len(header)):
             #for i in range(len(header)):
                 #if (header[i] in samples2):
                 if (header[i] in samples):
                    results.append(contents[i])

      for result in results:
          outfile.write(result+"\n")
