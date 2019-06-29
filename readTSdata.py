import io

dataDir = r'C:\Users\Michael\Documents\Visual Studio 2010\Projects\DATA'

colNames = ["Date","Time","Open","High","Low","Close","Up","Down"]


def readFile(filename):
    dataset = {}
    count = 0

    pathname = dataDir + '\\' + filename
    f = open(pathname, 'r')

    # discard the first line that has the column names
    r = f.readline().rstrip(chr(10))
    
    r = f.readline().rstrip(chr(10)) 
    while r:
        datapoint = {}
        #print r
        data = r.split(',')
        for i in range(len(colNames)):
            datapoint[colNames[i]] = data[i]

        index = datapoint["Date"] + ":" + datapoint["Time"]
        dataset[index] = datapoint

        count += 1
        #if count % 100 == 0: print count
        
        r = f.readline().rstrip(chr(10))

    f.close()
    
    print "Read %d lines from file '%s'." % (count, filename)
    
    return dataset


if __name__ == '__main__':
    
    dataCL = readFile('CL 2012-03-10.txt')
    dataDX = readFile('DX 2012-03-10.txt')
    dataHG = readFile('HG 2012-03-10.txt')
    dataYM = readFile('YM 2012-03-10.txt')

    commonKeys = []
    
    for k in dataCL.keys():
        if dataDX.has_key(k) and dataHG.has_key(k) and dataYM.has_key(k):
            commonKeys.append(k)

    print "%d keys in common." % len(commonKeys)

    dataset = {}
    for k in commonKeys:
        datapoint = {}
        dCL = float(dataCL[k]['Close']) - float(dataCL[k]['Open'])
        dDX = float(dataDX[k]['Close']) - float(dataDX[k]['Open'])
        dYM = float(dataYM[k]['Close']) - float(dataYM[k]['Open'])
        dHG = float(dataHG[k]['Close']) - float(dataHG[k]['Open'])
        datapoint['CL'] = dCL
        datapoint['DX'] = dDX
        datapoint['YM'] = dYM
        datapoint['HG'] = dHG
        dataset[k] = datapoint

    outputFilename = 'output 2012-03-10.txt'
    f = open(dataDir + '\\' + outputFilename, 'w')
    for k in dataset.keys():
        dp = dataset[k]
        f.write("%s,%f,%f,%f,%f\n" % (k, dp['CL'], dp['DX'], dp['YM'], dp['HG']))

    f.close()

    print "Wrote %d data points to '%s'." % (len(dataset.keys()), outputFilename)
                                             
    
    

        
        
        
    
