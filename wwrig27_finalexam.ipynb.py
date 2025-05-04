{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {
    "papermill": {
     "duration": 0.016104,
     "end_time": "2025-05-04T07:49:40.891686",
     "exception": false,
     "start_time": "2025-05-04T07:49:40.875582",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "# ISDS 3002 Final Exam"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "papermill": {
     "duration": 0.015106,
     "end_time": "2025-05-04T07:49:40.921655",
     "exception": false,
     "start_time": "2025-05-04T07:49:40.906549",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "**This is an individual assignment.  Do not discuss the questions or your answers with anyone other than Dr. Davis.**\n",
    "Turn in via Moodle.  Late exams will not be accepted.  No exceptions. Save your file as your pawsid + '_ISDS3002_final.ipynb' and upload it to Moodle before the due date.  As an example, 'jdavi48_ISDS3002_final.ipynb' is a proper file name.  \n",
    "\n",
    "When grading, I will open the file and select 'Run All'.  Your submitted file should be able to run and access the referenced datasets remotely (don't download the datasets...use the URLs provided).   \n",
    "\n",
    "Minus 5 points for naming the file incorrectly.\n",
    "\n",
    "Minus 15 points for submitting broken code that prohibits subsequent cells from running.\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "papermill": {
     "duration": 0.015446,
     "end_time": "2025-05-04T07:49:40.951955",
     "exception": false,
     "start_time": "2025-05-04T07:49:40.936509",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "**Question 1.** Scenario: You have some data where customer's last & first names are listed in one field, \"Davis, James\".  You are tasked to create a python function named 'parse_name' that will accept a string input and return a **list** with the names seperated and ordered by first name and then last name.  Create the function in the cell below. (10 points)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {
    "execution": {
     "iopub.execute_input": "2025-05-04T07:49:40.989442Z",
     "iopub.status.busy": "2025-05-04T07:49:40.988710Z",
     "iopub.status.idle": "2025-05-04T07:49:40.991582Z",
     "shell.execute_reply": "2025-05-04T07:49:40.991085Z",
     "shell.execute_reply.started": "2025-05-04T07:43:15.851390Z"
    },
    "papermill": {
     "duration": 0.023132,
     "end_time": "2025-05-04T07:49:40.991707",
     "exception": false,
     "start_time": "2025-05-04T07:49:40.968575",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [],
   "source": [
    "# write the code for your parse_name function here:\n",
    "def parse_name(name):\n",
    "    name_list = name.split(', ')\n",
    "    first_name = name_list[1]\n",
    "    last_name = name_list[0]\n",
    "    return [first_name, last_name]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {
    "execution": {
     "iopub.execute_input": "2025-05-04T07:49:41.028074Z",
     "iopub.status.busy": "2025-05-04T07:49:41.027323Z",
     "iopub.status.idle": "2025-05-04T07:49:41.030498Z",
     "shell.execute_reply": "2025-05-04T07:49:41.030999Z",
     "shell.execute_reply.started": "2025-05-04T07:43:15.861150Z"
    },
    "papermill": {
     "duration": 0.023999,
     "end_time": "2025-05-04T07:49:41.031149",
     "exception": false,
     "start_time": "2025-05-04T07:49:41.007150",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['James', 'Davis']"
      ]
     },
     "execution_count": 2,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "parse_name('Davis, James')\n",
    "# Do not change anything in this cell.\n",
    "# Running this cell should return the exact output:\n",
    "# ['James', 'Davis']"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "papermill": {
     "duration": 0.014552,
     "end_time": "2025-05-04T07:49:41.061056",
     "exception": false,
     "start_time": "2025-05-04T07:49:41.046504",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "**Question 2.** Scenario: Your team is working with data where dates are caputred as a string, \"9/15/2019\".  You are tasked to create a python function named 'mdy_date' that will accept a string input, convert it to a python **datetime** object, and return the **datetime** object.  Create the function in the cell below. (10 points)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {
    "execution": {
     "iopub.execute_input": "2025-05-04T07:49:41.097495Z",
     "iopub.status.busy": "2025-05-04T07:49:41.096572Z",
     "iopub.status.idle": "2025-05-04T07:49:41.099758Z",
     "shell.execute_reply": "2025-05-04T07:49:41.099290Z",
     "shell.execute_reply.started": "2025-05-04T07:43:15.884141Z"
    },
    "papermill": {
     "duration": 0.023687,
     "end_time": "2025-05-04T07:49:41.099898",
     "exception": false,
     "start_time": "2025-05-04T07:49:41.076211",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [],
   "source": [
    "# write the code for your mdy_date function here:\n",
    "import datetime\n",
    "\n",
    "def mdy_date(d):\n",
    "    dto = d. split('/') \n",
    "    return datetime.datetime(int(dto[-1]), int(dto[0]), int(dto[1]))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {
    "execution": {
     "iopub.execute_input": "2025-05-04T07:49:41.134694Z",
     "iopub.status.busy": "2025-05-04T07:49:41.133825Z",
     "iopub.status.idle": "2025-05-04T07:49:41.137635Z",
     "shell.execute_reply": "2025-05-04T07:49:41.138084Z",
     "shell.execute_reply.started": "2025-05-04T07:43:15.900797Z"
    },
    "papermill": {
     "duration": 0.023179,
     "end_time": "2025-05-04T07:49:41.138248",
     "exception": false,
     "start_time": "2025-05-04T07:49:41.115069",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "datetime.datetime(2019, 9, 15, 0, 0)"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "mdy_date(\"9/15/2019\")\n",
    "# Do not change anything in this cell.\n",
    "# Running this cell should return the exact output:\n",
    "# datetime.datetime(2019, 9, 15, 0, 0)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "papermill": {
     "duration": 0.015087,
     "end_time": "2025-05-04T07:49:41.168503",
     "exception": false,
     "start_time": "2025-05-04T07:49:41.153416",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "For questions 3 - 13, use the IMDb movies dataset located at [http://bit.ly/imdbratings](http://bit.ly/imdbratings)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "papermill": {
     "duration": 0.01498,
     "end_time": "2025-05-04T07:49:41.198714",
     "exception": false,
     "start_time": "2025-05-04T07:49:41.183734",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "**Question 3.** Import the pandas package in the conventional manner used in class and then read the IMDb movie dataset into a Pandas dataframe called 'df_movies' (5 points)."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {
    "execution": {
     "iopub.execute_input": "2025-05-04T07:49:41.236597Z",
     "iopub.status.busy": "2025-05-04T07:49:41.235931Z",
     "iopub.status.idle": "2025-05-04T07:49:41.248823Z",
     "shell.execute_reply": "2025-05-04T07:49:41.248316Z",
     "shell.execute_reply.started": "2025-05-04T07:43:15.916156Z"
    },
    "papermill": {
     "duration": 0.034916,
     "end_time": "2025-05-04T07:49:41.248963",
     "exception": false,
     "start_time": "2025-05-04T07:49:41.214047",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "df_movies = pd.read_csv('/kaggle/input/imdbdataset/imdb.csv')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "papermill": {
     "duration": 0.014835,
     "end_time": "2025-05-04T07:49:41.279168",
     "exception": false,
     "start_time": "2025-05-04T07:49:41.264333",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "**Question 4.** Using the 'head' method, view the first 15 rows of df_movies (5 points)."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {
    "execution": {
     "iopub.execute_input": "2025-05-04T07:49:41.330467Z",
     "iopub.status.busy": "2025-05-04T07:49:41.329737Z",
     "iopub.status.idle": "2025-05-04T07:49:41.340574Z",
     "shell.execute_reply": "2025-05-04T07:49:41.340071Z",
     "shell.execute_reply.started": "2025-05-04T07:43:15.936772Z"
    },
    "papermill": {
     "duration": 0.046369,
     "end_time": "2025-05-04T07:49:41.340688",
     "exception": false,
     "start_time": "2025-05-04T07:49:41.294319",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>star_rating</th>\n",
       "      <th>title</th>\n",
       "      <th>content_rating</th>\n",
       "      <th>genre</th>\n",
       "      <th>duration</th>\n",
       "      <th>actors_list</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>7.5</td>\n",
       "      <td>Bad Education</td>\n",
       "      <td>NC-17</td>\n",
       "      <td>Crime</td>\n",
       "      <td>106</td>\n",
       "      <td>[u'Gael Garc\\xeda Bernal', u'Fele Mart\\xednez'...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>7.8</td>\n",
       "      <td>Donnie Brasco</td>\n",
       "      <td>R</td>\n",
       "      <td>Biography</td>\n",
       "      <td>127</td>\n",
       "      <td>[u'Al Pacino', u'Johnny Depp', u'Michael Madsen']</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>7.8</td>\n",
       "      <td>The Sandlot</td>\n",
       "      <td>PG</td>\n",
       "      <td>Comedy</td>\n",
       "      <td>101</td>\n",
       "      <td>[u'Tom Guiry', u'Mike Vitar', u'Patrick Renna']</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>7.7</td>\n",
       "      <td>Blood Simple.</td>\n",
       "      <td>R</td>\n",
       "      <td>Crime</td>\n",
       "      <td>99</td>\n",
       "      <td>[u'John Getz', u'Frances McDormand', u'Dan Hed...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>7.7</td>\n",
       "      <td>50/50</td>\n",
       "      <td>R</td>\n",
       "      <td>Comedy</td>\n",
       "      <td>100</td>\n",
       "      <td>[u'Joseph Gordon-Levitt', u'Seth Rogen', u'Ann...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>8.9</td>\n",
       "      <td>The Lord of the Rings: The Return of the King</td>\n",
       "      <td>PG-13</td>\n",
       "      <td>Adventure</td>\n",
       "      <td>201</td>\n",
       "      <td>[u'Elijah Wood', u'Viggo Mortensen', u'Ian McK...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>8.0</td>\n",
       "      <td>The Exorcist</td>\n",
       "      <td>R</td>\n",
       "      <td>Horror</td>\n",
       "      <td>122</td>\n",
       "      <td>[u'Ellen Burstyn', u'Max von Sydow', u'Linda B...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7</th>\n",
       "      <td>8.2</td>\n",
       "      <td>Trainspotting</td>\n",
       "      <td>R</td>\n",
       "      <td>Drama</td>\n",
       "      <td>94</td>\n",
       "      <td>[u'Ewan McGregor', u'Ewen Bremner', u'Jonny Le...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8</th>\n",
       "      <td>8.6</td>\n",
       "      <td>The Intouchables</td>\n",
       "      <td>R</td>\n",
       "      <td>Biography</td>\n",
       "      <td>112</td>\n",
       "      <td>[u'Fran\\xe7ois Cluzet', u'Omar Sy', u'Anne Le ...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>9</th>\n",
       "      <td>8.3</td>\n",
       "      <td>The Gold Rush</td>\n",
       "      <td>NOT RATED</td>\n",
       "      <td>Adventure</td>\n",
       "      <td>95</td>\n",
       "      <td>[u'Charles Chaplin', u'Mack Swain', u'Tom Murr...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>10</th>\n",
       "      <td>7.4</td>\n",
       "      <td>Blue Valentine</td>\n",
       "      <td>NC-17</td>\n",
       "      <td>Drama</td>\n",
       "      <td>112</td>\n",
       "      <td>[u'Ryan Gosling', u'Michelle Williams', u'John...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>11</th>\n",
       "      <td>7.6</td>\n",
       "      <td>Ghost Dog: The Way of the Samurai</td>\n",
       "      <td>R</td>\n",
       "      <td>Action</td>\n",
       "      <td>116</td>\n",
       "      <td>[u'Forest Whitaker', u'Henry Silva', u'John To...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>12</th>\n",
       "      <td>7.8</td>\n",
       "      <td>Sabrina</td>\n",
       "      <td>UNRATED</td>\n",
       "      <td>Comedy</td>\n",
       "      <td>113</td>\n",
       "      <td>[u'Humphrey Bogart', u'Audrey Hepburn', u'Will...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>13</th>\n",
       "      <td>7.6</td>\n",
       "      <td>The Raid: Redemption</td>\n",
       "      <td>R</td>\n",
       "      <td>Action</td>\n",
       "      <td>101</td>\n",
       "      <td>[u'Iko Uwais', u'Ananda George', u'Ray Sahetapy']</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>14</th>\n",
       "      <td>7.8</td>\n",
       "      <td>Breakfast at Tiffany's</td>\n",
       "      <td>NOT RATED</td>\n",
       "      <td>Comedy</td>\n",
       "      <td>115</td>\n",
       "      <td>[u'Audrey Hepburn', u'George Peppard', u'Patri...</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "    star_rating                                          title content_rating  \\\n",
       "0           7.5                                  Bad Education          NC-17   \n",
       "1           7.8                                  Donnie Brasco              R   \n",
       "2           7.8                                    The Sandlot             PG   \n",
       "3           7.7                                  Blood Simple.              R   \n",
       "4           7.7                                          50/50              R   \n",
       "5           8.9  The Lord of the Rings: The Return of the King          PG-13   \n",
       "6           8.0                                   The Exorcist              R   \n",
       "7           8.2                                  Trainspotting              R   \n",
       "8           8.6                               The Intouchables              R   \n",
       "9           8.3                                  The Gold Rush      NOT RATED   \n",
       "10          7.4                                 Blue Valentine          NC-17   \n",
       "11          7.6              Ghost Dog: The Way of the Samurai              R   \n",
       "12          7.8                                        Sabrina        UNRATED   \n",
       "13          7.6                           The Raid: Redemption              R   \n",
       "14          7.8                         Breakfast at Tiffany's      NOT RATED   \n",
       "\n",
       "        genre  duration                                        actors_list  \n",
       "0       Crime       106  [u'Gael Garc\\xeda Bernal', u'Fele Mart\\xednez'...  \n",
       "1   Biography       127  [u'Al Pacino', u'Johnny Depp', u'Michael Madsen']  \n",
       "2      Comedy       101    [u'Tom Guiry', u'Mike Vitar', u'Patrick Renna']  \n",
       "3       Crime        99  [u'John Getz', u'Frances McDormand', u'Dan Hed...  \n",
       "4      Comedy       100  [u'Joseph Gordon-Levitt', u'Seth Rogen', u'Ann...  \n",
       "5   Adventure       201  [u'Elijah Wood', u'Viggo Mortensen', u'Ian McK...  \n",
       "6      Horror       122  [u'Ellen Burstyn', u'Max von Sydow', u'Linda B...  \n",
       "7       Drama        94  [u'Ewan McGregor', u'Ewen Bremner', u'Jonny Le...  \n",
       "8   Biography       112  [u'Fran\\xe7ois Cluzet', u'Omar Sy', u'Anne Le ...  \n",
       "9   Adventure        95  [u'Charles Chaplin', u'Mack Swain', u'Tom Murr...  \n",
       "10      Drama       112  [u'Ryan Gosling', u'Michelle Williams', u'John...  \n",
       "11     Action       116  [u'Forest Whitaker', u'Henry Silva', u'John To...  \n",
       "12     Comedy       113  [u'Humphrey Bogart', u'Audrey Hepburn', u'Will...  \n",
       "13     Action       101  [u'Iko Uwais', u'Ananda George', u'Ray Sahetapy']  \n",
       "14     Comedy       115  [u'Audrey Hepburn', u'George Peppard', u'Patri...  "
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df_movies.head(15)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "papermill": {
     "duration": 0.015609,
     "end_time": "2025-05-04T07:49:41.372155",
     "exception": false,
     "start_time": "2025-05-04T07:49:41.356546",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "**Question 5.** Use the proper method, and only one method, to display the descriptive statistics for the numeric columns (count, mean, std, min, 25%, 50%, 75%, max) for df_movies. (5 points)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {
    "execution": {
     "iopub.execute_input": "2025-05-04T07:49:41.415104Z",
     "iopub.status.busy": "2025-05-04T07:49:41.414444Z",
     "iopub.status.idle": "2025-05-04T07:49:41.427354Z",
     "shell.execute_reply": "2025-05-04T07:49:41.426826Z",
     "shell.execute_reply.started": "2025-05-04T07:43:15.960286Z"
    },
    "papermill": {
     "duration": 0.039402,
     "end_time": "2025-05-04T07:49:41.427476",
     "exception": false,
     "start_time": "2025-05-04T07:49:41.388074",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>star_rating</th>\n",
       "      <th>duration</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>count</th>\n",
       "      <td>979.000000</td>\n",
       "      <td>979.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>mean</th>\n",
       "      <td>7.889785</td>\n",
       "      <td>120.979571</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>std</th>\n",
       "      <td>0.336069</td>\n",
       "      <td>26.218010</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>min</th>\n",
       "      <td>7.400000</td>\n",
       "      <td>64.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>25%</th>\n",
       "      <td>7.600000</td>\n",
       "      <td>102.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>50%</th>\n",
       "      <td>7.800000</td>\n",
       "      <td>117.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>75%</th>\n",
       "      <td>8.100000</td>\n",
       "      <td>134.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>max</th>\n",
       "      <td>9.300000</td>\n",
       "      <td>242.000000</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "       star_rating    duration\n",
       "count   979.000000  979.000000\n",
       "mean      7.889785  120.979571\n",
       "std       0.336069   26.218010\n",
       "min       7.400000   64.000000\n",
       "25%       7.600000  102.000000\n",
       "50%       7.800000  117.000000\n",
       "75%       8.100000  134.000000\n",
       "max       9.300000  242.000000"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df_movies.describe()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "papermill": {
     "duration": 0.015865,
     "end_time": "2025-05-04T07:49:41.459541",
     "exception": false,
     "start_time": "2025-05-04T07:49:41.443676",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "**Question 6.** Rename the 'star_rating' column to 'stars' and 'content_rating' to 'rated'.  Output the column names using the correct method. (10 points)."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {
    "execution": {
     "iopub.execute_input": "2025-05-04T07:49:41.498610Z",
     "iopub.status.busy": "2025-05-04T07:49:41.497657Z",
     "iopub.status.idle": "2025-05-04T07:49:41.501381Z",
     "shell.execute_reply": "2025-05-04T07:49:41.500737Z",
     "shell.execute_reply.started": "2025-05-04T07:43:16.040168Z"
    },
    "papermill": {
     "duration": 0.025854,
     "end_time": "2025-05-04T07:49:41.501499",
     "exception": false,
     "start_time": "2025-05-04T07:49:41.475645",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Index(['stars', 'title', 'rated', 'genre', 'duration', 'actors_list'], dtype='object')"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df_movies.rename(columns = {'star_rating': 'stars', 'content_rating': 'rated'}, inplace=True)\n",
    "df_movies.columns\n",
    "# output should be: Index(['stars', 'title', 'rated', 'genre', 'duration', 'actors_list'], dtype='object')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "papermill": {
     "duration": 0.017505,
     "end_time": "2025-05-04T07:49:41.535341",
     "exception": false,
     "start_time": "2025-05-04T07:49:41.517836",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "**Question 7.** Using a single line of code, calculate the average movie duration by genre. (5 points)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {
    "execution": {
     "iopub.execute_input": "2025-05-04T07:49:41.577779Z",
     "iopub.status.busy": "2025-05-04T07:49:41.576800Z",
     "iopub.status.idle": "2025-05-04T07:49:41.580268Z",
     "shell.execute_reply": "2025-05-04T07:49:41.580693Z",
     "shell.execute_reply.started": "2025-05-04T07:43:16.052633Z"
    },
    "papermill": {
     "duration": 0.028948,
     "end_time": "2025-05-04T07:49:41.580839",
     "exception": false,
     "start_time": "2025-05-04T07:49:41.551891",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "genre\n",
       "Action       126.485294\n",
       "Adventure    134.840000\n",
       "Animation     96.596774\n",
       "Biography    131.844156\n",
       "Comedy       107.602564\n",
       "Crime        122.298387\n",
       "Drama        126.539568\n",
       "Family       107.500000\n",
       "Fantasy      112.000000\n",
       "Film-Noir     97.333333\n",
       "History       66.000000\n",
       "Horror       102.517241\n",
       "Mystery      115.625000\n",
       "Sci-Fi       109.000000\n",
       "Thriller     114.200000\n",
       "Western      136.666667\n",
       "Name: duration, dtype: float64"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df_movies.groupby(['genre']).duration.mean()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "papermill": {
     "duration": 0.016298,
     "end_time": "2025-05-04T07:49:41.613947",
     "exception": false,
     "start_time": "2025-05-04T07:49:41.597649",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "**Question 8.**  Using your output from above, which genre has the longest duration? (5 points)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "papermill": {
     "duration": 0.016502,
     "end_time": "2025-05-04T07:49:41.647007",
     "exception": false,
     "start_time": "2025-05-04T07:49:41.630505",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "put your question 8 answer here."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {
    "execution": {
     "iopub.execute_input": "2025-05-04T07:49:41.693160Z",
     "iopub.status.busy": "2025-05-04T07:49:41.685787Z",
     "iopub.status.idle": "2025-05-04T07:49:41.698609Z",
     "shell.execute_reply": "2025-05-04T07:49:41.698149Z",
     "shell.execute_reply.started": "2025-05-04T07:43:16.078681Z"
    },
    "papermill": {
     "duration": 0.034752,
     "end_time": "2025-05-04T07:49:41.698722",
     "exception": false,
     "start_time": "2025-05-04T07:49:41.663970",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "genre\n",
       "Western    136.666667\n",
       "Name: duration, dtype: float64"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df_movies.groupby(['genre'])['duration'].mean().nlargest(1)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "papermill": {
     "duration": 0.016607,
     "end_time": "2025-05-04T07:49:41.732204",
     "exception": false,
     "start_time": "2025-05-04T07:49:41.715597",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "**Question 9.** Import matplotlib.pyplot and the seaborn package using the conventions from class.  Make sure to designate any plotting images be displayed inline. (5 points)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {
    "execution": {
     "iopub.execute_input": "2025-05-04T07:49:41.773030Z",
     "iopub.status.busy": "2025-05-04T07:49:41.772352Z",
     "iopub.status.idle": "2025-05-04T07:49:42.612816Z",
     "shell.execute_reply": "2025-05-04T07:49:42.612323Z",
     "shell.execute_reply.started": "2025-05-04T07:43:16.096917Z"
    },
    "papermill": {
     "duration": 0.863794,
     "end_time": "2025-05-04T07:49:42.612956",
     "exception": false,
     "start_time": "2025-05-04T07:49:41.749162",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [],
   "source": [
    "%matplotlib inline\n",
    "import matplotlib.pyplot as plt\n",
    "import seaborn as sns"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "papermill": {
     "duration": 0.017861,
     "end_time": "2025-05-04T07:49:42.648090",
     "exception": false,
     "start_time": "2025-05-04T07:49:42.630229",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "**Question 10.** In the 'rated' column, replace instances of 'NOT RATED' and 'UNRATED' with 'N/R' and replace 'APPROVED', 'PASSED' and 'GP' with 'OTHER'.  Output the last 10 rows using the tail method. (10 points)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {
    "execution": {
     "iopub.execute_input": "2025-05-04T07:49:42.697942Z",
     "iopub.status.busy": "2025-05-04T07:49:42.696932Z",
     "iopub.status.idle": "2025-05-04T07:49:42.700245Z",
     "shell.execute_reply": "2025-05-04T07:49:42.700698Z",
     "shell.execute_reply.started": "2025-05-04T07:43:17.305109Z"
    },
    "papermill": {
     "duration": 0.035479,
     "end_time": "2025-05-04T07:49:42.700836",
     "exception": false,
     "start_time": "2025-05-04T07:49:42.665357",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>stars</th>\n",
       "      <th>title</th>\n",
       "      <th>rated</th>\n",
       "      <th>genre</th>\n",
       "      <th>duration</th>\n",
       "      <th>actors_list</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>969</th>\n",
       "      <td>7.5</td>\n",
       "      <td>Notes on a Scandal</td>\n",
       "      <td>R</td>\n",
       "      <td>Drama</td>\n",
       "      <td>92</td>\n",
       "      <td>[u'Cate Blanchett', u'Judi Dench', u'Andrew Si...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>970</th>\n",
       "      <td>7.8</td>\n",
       "      <td>Changeling</td>\n",
       "      <td>R</td>\n",
       "      <td>Drama</td>\n",
       "      <td>141</td>\n",
       "      <td>[u'Angelina Jolie', u'Colm Feore', u'Amy Ryan']</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>971</th>\n",
       "      <td>8.6</td>\n",
       "      <td>Whiplash</td>\n",
       "      <td>R</td>\n",
       "      <td>Drama</td>\n",
       "      <td>107</td>\n",
       "      <td>[u'Miles Teller', u'J.K. Simmons', u'Melissa B...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>972</th>\n",
       "      <td>7.4</td>\n",
       "      <td>The Rock</td>\n",
       "      <td>R</td>\n",
       "      <td>Action</td>\n",
       "      <td>136</td>\n",
       "      <td>[u'Sean Connery', u'Nicolas Cage', u'Ed Harris']</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>973</th>\n",
       "      <td>8.1</td>\n",
       "      <td>The Philadelphia Story</td>\n",
       "      <td>N/R</td>\n",
       "      <td>Comedy</td>\n",
       "      <td>112</td>\n",
       "      <td>[u'Cary Grant', u'Katharine Hepburn', u'James ...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>974</th>\n",
       "      <td>7.8</td>\n",
       "      <td>The Birds</td>\n",
       "      <td>PG-13</td>\n",
       "      <td>Horror</td>\n",
       "      <td>119</td>\n",
       "      <td>[u'Rod Taylor', u'Tippi Hedren', u'Suzanne Ple...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>975</th>\n",
       "      <td>8.5</td>\n",
       "      <td>Apocalypse Now</td>\n",
       "      <td>R</td>\n",
       "      <td>Drama</td>\n",
       "      <td>153</td>\n",
       "      <td>[u'Martin Sheen', u'Marlon Brando', u'Robert D...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>976</th>\n",
       "      <td>7.7</td>\n",
       "      <td>Moulin Rouge!</td>\n",
       "      <td>PG-13</td>\n",
       "      <td>Drama</td>\n",
       "      <td>127</td>\n",
       "      <td>[u'Nicole Kidman', u'Ewan McGregor', u'John Le...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>977</th>\n",
       "      <td>7.6</td>\n",
       "      <td>Of Mice and Men</td>\n",
       "      <td>PG-13</td>\n",
       "      <td>Drama</td>\n",
       "      <td>115</td>\n",
       "      <td>[u'John Malkovich', u'Gary Sinise', u'Ray Wals...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>978</th>\n",
       "      <td>7.8</td>\n",
       "      <td>The Theory of Everything</td>\n",
       "      <td>PG-13</td>\n",
       "      <td>Biography</td>\n",
       "      <td>123</td>\n",
       "      <td>[u'Eddie Redmayne', u'Felicity Jones', u'Tom P...</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "     stars                     title  rated      genre  duration  \\\n",
       "969    7.5        Notes on a Scandal      R      Drama        92   \n",
       "970    7.8                Changeling      R      Drama       141   \n",
       "971    8.6                  Whiplash      R      Drama       107   \n",
       "972    7.4                  The Rock      R     Action       136   \n",
       "973    8.1    The Philadelphia Story    N/R     Comedy       112   \n",
       "974    7.8                 The Birds  PG-13     Horror       119   \n",
       "975    8.5            Apocalypse Now      R      Drama       153   \n",
       "976    7.7             Moulin Rouge!  PG-13      Drama       127   \n",
       "977    7.6           Of Mice and Men  PG-13      Drama       115   \n",
       "978    7.8  The Theory of Everything  PG-13  Biography       123   \n",
       "\n",
       "                                           actors_list  \n",
       "969  [u'Cate Blanchett', u'Judi Dench', u'Andrew Si...  \n",
       "970    [u'Angelina Jolie', u'Colm Feore', u'Amy Ryan']  \n",
       "971  [u'Miles Teller', u'J.K. Simmons', u'Melissa B...  \n",
       "972   [u'Sean Connery', u'Nicolas Cage', u'Ed Harris']  \n",
       "973  [u'Cary Grant', u'Katharine Hepburn', u'James ...  \n",
       "974  [u'Rod Taylor', u'Tippi Hedren', u'Suzanne Ple...  \n",
       "975  [u'Martin Sheen', u'Marlon Brando', u'Robert D...  \n",
       "976  [u'Nicole Kidman', u'Ewan McGregor', u'John Le...  \n",
       "977  [u'John Malkovich', u'Gary Sinise', u'Ray Wals...  \n",
       "978  [u'Eddie Redmayne', u'Felicity Jones', u'Tom P...  "
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df_movies.rated.replace(['NOT RATED', 'UNRATED'], \"N/R\", inplace=True)\n",
    "df_movies.rated.replace(['APPROVED', 'PASSED','GP'], 'OTHER', inplace=True)\n",
    "df_movies.tail(10)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "papermill": {
     "duration": 0.01715,
     "end_time": "2025-05-04T07:49:42.735688",
     "exception": false,
     "start_time": "2025-05-04T07:49:42.718538",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "**Question 11.**  Using the seaborn package output a countplot of the ratings (R, PG-13, ....) on the x-axis.  Rotate the xticks 45 degrees for better readibility. (15 points)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {
    "execution": {
     "iopub.execute_input": "2025-05-04T07:49:42.779849Z",
     "iopub.status.busy": "2025-05-04T07:49:42.776133Z",
     "iopub.status.idle": "2025-05-04T07:49:42.939965Z",
     "shell.execute_reply": "2025-05-04T07:49:42.939457Z",
     "shell.execute_reply.started": "2025-05-04T07:43:17.325609Z"
    },
    "papermill": {
     "duration": 0.186841,
     "end_time": "2025-05-04T07:49:42.940089",
     "exception": false,
     "start_time": "2025-05-04T07:49:42.753248",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(array([0, 1, 2, 3, 4, 5, 6, 7, 8]),\n",
       " <a list of 9 Text major ticklabel objects>)"
      ]
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.countplot(x=\"rated\", data=df_movies)\n",
    "plt.xlabel('Ratings')\n",
    "plt.xticks(rotation=45)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "papermill": {
     "duration": 0.018443,
     "end_time": "2025-05-04T07:49:42.978026",
     "exception": false,
     "start_time": "2025-05-04T07:49:42.959583",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "**Question 12.**  Display only the dataframe rows for movies awarded over 8.8 stars. (10 points)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {
    "execution": {
     "iopub.execute_input": "2025-05-04T07:49:43.019735Z",
     "iopub.status.busy": "2025-05-04T07:49:43.019122Z",
     "iopub.status.idle": "2025-05-04T07:49:43.046154Z",
     "shell.execute_reply": "2025-05-04T07:49:43.045622Z",
     "shell.execute_reply.started": "2025-05-04T07:43:17.550676Z"
    },
    "papermill": {
     "duration": 0.04985,
     "end_time": "2025-05-04T07:49:43.046295",
     "exception": false,
     "start_time": "2025-05-04T07:49:42.996445",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>stars</th>\n",
       "      <th>title</th>\n",
       "      <th>rated</th>\n",
       "      <th>genre</th>\n",
       "      <th>duration</th>\n",
       "      <th>actors_list</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>8.9</td>\n",
       "      <td>The Lord of the Rings: The Return of the King</td>\n",
       "      <td>PG-13</td>\n",
       "      <td>Adventure</td>\n",
       "      <td>201</td>\n",
       "      <td>[u'Elijah Wood', u'Viggo Mortensen', u'Ian McK...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>32</th>\n",
       "      <td>9.3</td>\n",
       "      <td>The Shawshank Redemption</td>\n",
       "      <td>R</td>\n",
       "      <td>Crime</td>\n",
       "      <td>142</td>\n",
       "      <td>[u'Tim Robbins', u'Morgan Freeman', u'Bob Gunt...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>94</th>\n",
       "      <td>9.1</td>\n",
       "      <td>The Godfather: Part II</td>\n",
       "      <td>R</td>\n",
       "      <td>Crime</td>\n",
       "      <td>200</td>\n",
       "      <td>[u'Al Pacino', u'Robert De Niro', u'Robert Duv...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>149</th>\n",
       "      <td>8.9</td>\n",
       "      <td>12 Angry Men</td>\n",
       "      <td>N/R</td>\n",
       "      <td>Drama</td>\n",
       "      <td>96</td>\n",
       "      <td>[u'Henry Fonda', u'Lee J. Cobb', u'Martin Bals...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>229</th>\n",
       "      <td>8.9</td>\n",
       "      <td>Schindler's List</td>\n",
       "      <td>R</td>\n",
       "      <td>Biography</td>\n",
       "      <td>195</td>\n",
       "      <td>[u'Liam Neeson', u'Ralph Fiennes', u'Ben Kings...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>534</th>\n",
       "      <td>8.9</td>\n",
       "      <td>Pulp Fiction</td>\n",
       "      <td>R</td>\n",
       "      <td>Crime</td>\n",
       "      <td>154</td>\n",
       "      <td>[u'John Travolta', u'Uma Thurman', u'Samuel L....</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>641</th>\n",
       "      <td>8.9</td>\n",
       "      <td>The Good, the Bad and the Ugly</td>\n",
       "      <td>N/R</td>\n",
       "      <td>Western</td>\n",
       "      <td>161</td>\n",
       "      <td>[u'Clint Eastwood', u'Eli Wallach', u'Lee Van ...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>671</th>\n",
       "      <td>8.9</td>\n",
       "      <td>Fight Club</td>\n",
       "      <td>R</td>\n",
       "      <td>Drama</td>\n",
       "      <td>139</td>\n",
       "      <td>[u'Brad Pitt', u'Edward Norton', u'Helena Bonh...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>704</th>\n",
       "      <td>9.2</td>\n",
       "      <td>The Godfather</td>\n",
       "      <td>R</td>\n",
       "      <td>Crime</td>\n",
       "      <td>175</td>\n",
       "      <td>[u'Marlon Brando', u'Al Pacino', u'James Caan']</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>921</th>\n",
       "      <td>9.0</td>\n",
       "      <td>The Dark Knight</td>\n",
       "      <td>PG-13</td>\n",
       "      <td>Action</td>\n",
       "      <td>152</td>\n",
       "      <td>[u'Christian Bale', u'Heath Ledger', u'Aaron E...</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "     stars                                          title  rated      genre  \\\n",
       "5      8.9  The Lord of the Rings: The Return of the King  PG-13  Adventure   \n",
       "32     9.3                       The Shawshank Redemption      R      Crime   \n",
       "94     9.1                         The Godfather: Part II      R      Crime   \n",
       "149    8.9                                   12 Angry Men    N/R      Drama   \n",
       "229    8.9                               Schindler's List      R  Biography   \n",
       "534    8.9                                   Pulp Fiction      R      Crime   \n",
       "641    8.9                 The Good, the Bad and the Ugly    N/R    Western   \n",
       "671    8.9                                     Fight Club      R      Drama   \n",
       "704    9.2                                  The Godfather      R      Crime   \n",
       "921    9.0                                The Dark Knight  PG-13     Action   \n",
       "\n",
       "     duration                                        actors_list  \n",
       "5         201  [u'Elijah Wood', u'Viggo Mortensen', u'Ian McK...  \n",
       "32        142  [u'Tim Robbins', u'Morgan Freeman', u'Bob Gunt...  \n",
       "94        200  [u'Al Pacino', u'Robert De Niro', u'Robert Duv...  \n",
       "149        96  [u'Henry Fonda', u'Lee J. Cobb', u'Martin Bals...  \n",
       "229       195  [u'Liam Neeson', u'Ralph Fiennes', u'Ben Kings...  \n",
       "534       154  [u'John Travolta', u'Uma Thurman', u'Samuel L....  \n",
       "641       161  [u'Clint Eastwood', u'Eli Wallach', u'Lee Van ...  \n",
       "671       139  [u'Brad Pitt', u'Edward Norton', u'Helena Bonh...  \n",
       "704       175    [u'Marlon Brando', u'Al Pacino', u'James Caan']  \n",
       "921       152  [u'Christian Bale', u'Heath Ledger', u'Aaron E...  "
      ]
     },
     "execution_count": 14,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df_movies[df_movies.stars > 8.8]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "papermill": {
     "duration": 0.018471,
     "end_time": "2025-05-04T07:49:43.084499",
     "exception": false,
     "start_time": "2025-05-04T07:49:43.066028",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "**Question 13.** Which of the movies in the above output is your favorite?  You must select from the output of the cell above.  (5 points)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "papermill": {
     "duration": 0.019892,
     "end_time": "2025-05-04T07:49:43.123172",
     "exception": false,
     "start_time": "2025-05-04T07:49:43.103280",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "put your answer here"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {
    "execution": {
     "iopub.execute_input": "2025-05-04T07:49:43.172791Z",
     "iopub.status.busy": "2025-05-04T07:49:43.172056Z",
     "iopub.status.idle": "2025-05-04T07:49:43.175728Z",
     "shell.execute_reply": "2025-05-04T07:49:43.175276Z",
     "shell.execute_reply.started": "2025-05-04T07:43:17.593906Z"
    },
    "papermill": {
     "duration": 0.033556,
     "end_time": "2025-05-04T07:49:43.175842",
     "exception": false,
     "start_time": "2025-05-04T07:49:43.142286",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>stars</th>\n",
       "      <th>title</th>\n",
       "      <th>rated</th>\n",
       "      <th>genre</th>\n",
       "      <th>duration</th>\n",
       "      <th>actors_list</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>921</th>\n",
       "      <td>9.0</td>\n",
       "      <td>The Dark Knight</td>\n",
       "      <td>PG-13</td>\n",
       "      <td>Action</td>\n",
       "      <td>152</td>\n",
       "      <td>[u'Christian Bale', u'Heath Ledger', u'Aaron E...</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "     stars            title  rated   genre  duration  \\\n",
       "921    9.0  The Dark Knight  PG-13  Action       152   \n",
       "\n",
       "                                           actors_list  \n",
       "921  [u'Christian Bale', u'Heath Ledger', u'Aaron E...  "
      ]
     },
     "execution_count": 15,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df_movies[df_movies.title == \"The Dark Knight\"]"
   ]
  }
 ],
 "metadata": {
  "kaggle": {
   "accelerator": "none",
   "dataSources": [
    {
     "datasetId": 1299063,
     "sourceId": 2164209,
     "sourceType": "datasetVersion"
    }
   ],
   "dockerImageVersionId": 30008,
   "isGpuEnabled": false,
   "isInternetEnabled": true,
   "language": "python",
   "sourceType": "notebook"
  },
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.6"
  },
  "papermill": {
   "duration": 6.426521,
   "end_time": "2025-05-04T07:49:43.302447",
   "environment_variables": {},
   "exception": null,
   "input_path": "__notebook__.ipynb",
   "output_path": "__notebook__.ipynb",
   "parameters": {},
   "start_time": "2025-05-04T07:49:36.875926",
   "version": "2.1.0"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
