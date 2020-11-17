import io
k=0
with io.open("mk2.txt","r",encoding="utf-8") as f:
    lst=["import","imports","importing","imported"]
    with io.open("imports.txt","w",encoding="utf-8") as fimp:
        with io.open("ximports.txt","w",encoding="utf-8") as fximp:
            for i in f.readlines():
                k=0
                for j in lst:
                    
                    if(j in i):
                        k=1
                        fimp.write(i)
                        break
                if(k==0):
                    fximp.write(i)


with io.open("ximports.txt","r",encoding="utf-8") as f2:
    lst2=["export","exports","exporting","exported"]
    with io.open("exports.txt","w",encoding="utf-8") as fexp:
        with io.open("xexports.txt","w",encoding="utf-8") as fxexp:
            for i in f2.readlines():
                k=0
                for j in lst2:
                
                    if(j in i):
                        k=1
                        fexp.write(i)
                        break
                if(k==0):
                    fxexp.write(i)

with io.open("xexports.txt","r",encoding="utf-8") as f3:
    lst3=["service","services","servicing","serviced"]
    with io.open("services.txt","w",encoding="utf-8") as fser:
        with io.open("xservices.txt","w",encoding="utf-8") as fxser:
            for i in f3.readlines():
                k=0
                for j in lst3:
                
                    if(j in i):
                        k=1
                        fser.write(i)
                        break
                if(k==0):
                    fxser.write(i)


with io.open("xservices.txt","r",encoding="utf-8") as f4:
    lst4=["manufacture","manufactures","manufacturing","manufactured","production","produces","produced"]
    with io.open("manufactures.txt","w",encoding="utf-8") as fmanu:
        with io.open("xmanufactures.txt","w",encoding="utf-8") as fxmanu:
            for i in f4.readlines():
                k=0
                for j in lst4:
                
                    if(j in i):
                        k=1
                        fmanu.write(i)
                        break
                if(k==0):
                    fxmanu.write(i)


with io.open("xmanufactures.txt","r",encoding="utf-8") as f5:
    lst5=["agriculture","farming","farmers","farmer","crop","yeild"]
    with io.open("agri.txt","w",encoding="utf-8") as fagri:
        with io.open("xagri.txt","w",encoding="utf-8") as fxagri:
            for i in f5.readlines():
                k=0
                for j in lst5:
                
                    if(j in i):
                        k=1
                        fagri.write(i)
                        break
                if(k==0):
                    fxagri.write(i)

with io.open("xagri.txt","r",encoding="utf-8") as f5:
    lst5=["government","govt","India","Government","Pakistan","Tamil Nadu","Jammu","Ministry","Indian","Govt","BJP","Parliament","Congress","Delhi","President","Department","Bank","Tamil","PM","Minister","Modi"]
    with io.open("leftover.txt","w",encoding="utf-8") as fagri:
        with io.open("Industry.txt","w",encoding="utf-8") as fxagri:
            for i in f5.readlines():
                k=0
                for j in lst5:
                
                    if(j in i):
                        k=1
                        fagri.write(i)
                        break
                if(k==0):
                    fxagri.write(i)
