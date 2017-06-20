#!/usr/bin/env python
# -----------------------------------------------------------------------------
#  File:        train.py
#  Description: HO1 optimization example
#  Created:     10-Jan-2015 Harrison B. Prosper and Sezen Sekmen
#  Updated:     17-Jun-2017 HBP get ready for release
# -----------------------------------------------------------------------------
import os, sys, re
from string import *
try:
    from rgsutil import *
except:
    sys.exit("** first do\n\tsource setup.sh\n** to setup the RGS package")
try:
    from ROOT import *
except:
    sys.exit("** ROOT with PyROOT is needed to run this example")
# -----------------------------------------------------------------------------
# read scale factors
execfile('../../data/scales.py')
    
def main():
    NAME = 'HO1'
    print "="*80
    print "\t=== %s ===" % NAME
    print "="*80

    # ---------------------------------------------------------------------
    # Load the RGS shared library and check that the various input files
    # exist.
    # ---------------------------------------------------------------------
    gSystem.AddDynamicPath('$RGS_PATH/lib')
    if gSystem.Load("libRGS") < 0: error("unable to load libRGS")

    # Name of file containing cut definitions
    # Format of file:
    #   variable-name  cut-type (>, <, <>, |>, |<, ==)
    varfilename = "%s.cuts" % NAME
    if not os.path.exists(varfilename):
        error("unable to open variables file %s" % varfilename)

    # Name of signal file
    sigfilename  = "../../data/ntuple_HZZ4L_VBF.root"
    if not os.path.exists(sigfilename):
        error("unable to open signal file %s" % sigfilename)

    # Name of background file        
    bkgfilename1 = "../../data/ntuple_HZZ4L.root"
    if not os.path.exists(bkgfilename1):
        error("unable to open background file %s" % bkgfilename1)

    # Name of background file        
    bkgfilename2 = "../../data/ntuple_ZZ4L.root"
    if not os.path.exists(bkgfilename2):
        error("unable to open background file %s" % bkgfilename2)        

    # ---------------------------------------------------------------------
    #  Create RGS object
    #  
    #   The file (cutdatafilename) of cut-points is usually a signal file,
    #   which ideally differs from the signal file on which the RGS
    #   algorithm is run.
    # ---------------------------------------------------------------------
    cutdatafilename = sigfilename
    start      = 0           # start row 
    maxcuts    = 10000       # maximum number of cut-points to consider
    treename   = "Analysis"  # name of Root tree 
    weightname = "weight"    # name of event weight variable
    selection  = ""
    rgs = RGS(cutdatafilename, start, maxcuts, treename,
                  weightname, selection)

    # ---------------------------------------------------------------------
    #  Add signal and background data to RGS object.
    #  Weight each event using the value in the field weightname, if
    #  present.
    #  NB: We asssume all files are of the same format.
    # ---------------------------------------------------------------------
    # 1) The first optional argument is a string, which, if given, will be
    # appended to the "count" and "fraction" variables. The "count" variable
    # contains the number of events that pass per cut-point, while "fraction"
    # is count / total, where total is the total number of events per file.
    # If no string is given, the default is to append an integer to the
    # "count" and "fraction" variables, starting at 0, in the order in which
    # the files are added to the RGS object.
    # 2) The second optional argument is the weight to be assigned per file. If
    # omitted the default weight is 1.
    # 3) The third optional argument is the selection string. If omitted, the
    # selection provided in the constructor is used.    
    
    start    =  0   #  start row
    numrows  = -1   #  scan all the data from the files

    rgs.add(sigfilename,  start, numrows, "_VBF", VBFscale)
    rgs.add(bkgfilename1, start, numrows, "_ggF", ggFscale)
    rgs.add(bkgfilename2, start, numrows, "_ZZ",  ZZscale)

    print "VBF yield: %10.2f +/- %-10.2f" % (rgs.total(0), rgs.etotal(0))
    print "ggF yield: %10.2f +/- %-10.2f" % (rgs.total(1), rgs.etotal(1))
    print "ZZ  yield: %10.2f +/- %-10.2f" % (rgs.total(2), rgs.etotal(2))    
    # ---------------------------------------------------------------------	
    #  Run RGS and write out results
    # ---------------------------------------------------------------------	    
    rgs.run(varfilename)

    # Write to a root file
    rgsfilename = "%s.root" % NAME
    rgs.save(rgsfilename)
# -----------------------------------------------------------------------------
try:
    main()
except KeyboardInterrupt:
    print "\tciao!\n"



