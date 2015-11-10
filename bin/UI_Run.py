# -----------------------------------------------------------------------------
# Copyright * 2014, United States Government, as represented by the
# Administrator of the National Aeronautics and Space Administration. All
# rights reserved.
#
# The Crisis Mapping Toolkit (CMT) v1 platform is licensed under the Apache
# License, Version 2.0 (the "License"); you may not use this file except in
# compliance with the License. You may obtain a copy of the License at
# http://www.apache.org/licenses/LICENSE-2.0.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations under
# the License.
# -----------------------------------------------------------------------------

from PyQt4 import QtGui, QtCore
import sys
from LLAMA import Ui_Lake_Level_UI
from plot_water_levelui import *
from lake_measure_1_19_UIVersion import *

class Lake_Level_App(QtGui.QMainWindow, Ui_Lake_Level_UI):
    def __init__(self):
        # Explaining super is out of the scope of this article
        super(self.__class__, self).__init__()
        self.setupUi(self)

        self.algaeCheckbox.stateChanged.connect(self.algaeHandle)
        #self.graphCheckbox.stateChanged.connect(self.graphHandle)
        self.turbidityCheckbox.stateChanged.connect(self.turbidityHandle)
        self.tableCheckbox.stateChanged.connect(self.tableHandle)
        self.lake_areaCheckbox.stateChanged.connect(self.lake_areaHandle)
        self.start_date = '2000-01-01'
        self.end_date = '2000-01-01'
        self.selected_lake = 'Lake Tahoe'
        self.selectlakeDropMenu.activated[str].connect(self.selectLakeHandle)
        self.okBtn.clicked.connect(self.okHandle)
        self.endDate.dateChanged[QtCore.QDate].connect(self.endHandle)
        self.startDate.dateChanged[QtCore.QDate].connect(self.startHandle)

    def selectLakeHandle(self, text):
        self.selected_lake = str(text)

    def algaeHandle(self, state):
        if state == QtCore.Qt.Checked:
            self.algaeState = True
        else:
            self.algaeState = False

    def turbidityHandle(self, state):
        if state == QtCore.Qt.Checked:
            self.turbidityState = True
            print self.turbidityState
        else:
            self.turbidityState = False
            print self.turbidityState

    def graphHandle(self, state):
        if state == QtCore.Qt.Checked:
            self.graphState = True
            print self.graphState
        else:
            self.graphState = False
            print self.graphState

    def tableHandle(self, state):
        if state == QtCore.Qt.Checked:
            self.tableState = True
            print self.tableState
        else:
            self.tableState = False
            print self.tableState

    def lake_areaHandle(self, state):
        if state == QtCore.Qt.Checked:
            self.lake_areaState = True
            print self.lake_areaState
        else:
            self.lake_areaState = False
            print self.lake_areaState

    def startHandle(self, date):
        self.start_date = str(date.toString('yyyy-MM-dd'))

    def endHandle(self, date):
        self.end_date = str(date.toString('yyyy-MM-dd'))

    # def exporter(directory='C:\temp\\'):
    #     name_of_file = "export"
    #     l = [[1, 2], [2, 3], [4, 5]]
    #     completeName = os.path.abspath("C:/temp/%s.csv" % name_of_file)
    #     full_path = '%(directory)s\%(name_of_file)s.csv' % locals()
    #     out = open(full_path, "w")
    #     for row in l:
    #         for column in row:
    #             out.write('%d;' % column)
    #             out.write('\n')
    #         out.close()

    #QObject.connect(export, SIGNAL('clicked()'),exporter)

    def okHandle(self):
        #Add arguments to the lake_measure function. Arguments will consist of all the self.[INDEX] and
        #self.lake_areaHandle states. Possibly make window have a "Collect Data" tab and an "Analyze Data" tab. Possibly
        #a third tab or an option on "Collect Data" will allow user to get download URLs for rasters. Need to add
        #loading bar to lake_measure.py where X/cancel button will end the data search completely.
        if self.tableCheckbox.isChecked():
            table_water_level(self.selected_lake,
                             result_dir = 'C:\\Projects\\Fall 2015 - Lake Tahoe Water Resources\\Data\\Python Scripts\\UI_Script\\results')

        if self.graphCheckbox.isChecked():
            #Make plot water level a function, but add ability to search a set directory for the data file of the
            # selected lake. Will give warning if no data is found for that specific lake. Something like "Data not
            #found. Please retrieve data using 'Collect Data' and retry."
            plot_water_level(self.selected_lake,
                             result_dir = 'C:\\Projects\\Fall 2015 - Lake Tahoe Water Resources\\Data\\Python Scripts\\UI_Script\\results')

        if self.lake_areaCheckbox.isChecked():

            print 'Start date is:'+ self.start_date
            print 'End date is:' + self.end_date
            Lake_Level_Run(self.selected_lake, date = self.start_date, enddate = self.end_date,
                           results_dir = 'C:\\Projects\\Fall 2015 - Lake Tahoe Water Resources\\Data\\Python Scripts\\UI_Script\\results')
        # if self.tableState == True:
        #     water_level_table(self.selected_lake)
        #
        # if self.lake_areaState == True:
        #     Lake_Level_Run(self.selected_lake)


def main():
    app = QtGui.QApplication(sys.argv)  # A new instance of QApplication
    form = Lake_Level_App()                 # We set the form to be our ExampleApp (design)
    form.show()                         # Show the form
    app.exec_()                         # and execute the app


if __name__ == '__main__':              # if we're running file directly and not importing it
    main()
