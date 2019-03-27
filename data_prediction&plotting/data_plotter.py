"""This code interferes with the plotly to plot Scatterd 3D garph."""
import collections

import pickle
# import numpy as np
import random

import re

import plotly.graph_objs as go

import plotly.offline as py

import os


def plot_3dscattergraph(names, temp_sap, cgpa1, cgpa2, seq1, seq2, string_data, str1, str2):
    """Plot the 3D stattered graph by using WebGL application."""
    # y = np.random.multivariate_normal(np.array([0, 0, 0]), np.eye(3), 60).transpose()

    trace1 = go.Scatter3d(
        x=seq1,                             # names sequence
        y=seq2,                             # sap is randomized (decides the position on the graph i.e if 8 then 8th poistion or 8th line on the y axis)
        z=cgpa1,                            # cgpa
        mode='markers',
        marker=dict(
            size=8,
            color=cgpa1,                # set color to an array/list of desired values
            colorscale='Viridis',   # choose a colorscale              Blackbody, Viridis, Hot, Cividis, Electric
            opacity=1,
        )
    )

    if cgpa2 is not None:
        trace1 = go.Scatter3d(
            x=seq1,                             # names sequence
            y=seq2,                             # sap is randomized
            z=cgpa1,                            # cgpa
            mode='markers',
            marker=dict(
                size=6,
                color="red",
                opacity=0.6,
            ),
            name=str1,
        )
        trace2 = go.Scatter3d(
            x=seq1,                             # names sequence
            y=seq2,                             # sap is randomized
            z=cgpa2,                           # cgpa
            mode='markers',
            marker=dict(
                size=6,
                color="blue",
                opacity=0.6,
            ),
            name=str2,
        )
        data = [trace1, trace2]
    else:
        data = [trace1]

    layout = go.Layout(
        # autosize=False,
        # width=1000,
        # height=1000,
        title='Scatter 3d-Graph for ' + string_data,
        font=dict(family='Playfair Display', size=14, color='black'),
        margin=dict(
            l=5,
            r=5,
            b=5,
            t=60
        ),
        legend=dict(
            # orientation="h",
            # x=-0.1,
            # y=1.2,
            bgcolor='#E2E2E2',
            font=dict(
                family='Playfair Display',
                size=14,
                color='black'
            ),
        ),
        scene=go.layout.Scene(
            xaxis=go.layout.scene.XAxis(
                title="Students_Names",
                tickfont=dict(size=10),
                ticktext=names,             # plot names list as text
                tickvals=seq1,                 # plot numbers used to plot names as scale
                tickwidth=6,
                tickmode='array',
                spikecolor='#AF28F3',
                spikethickness=4,
                backgroundcolor="#54F0BC",
                showbackground=True,
                gridcolor='rgb(51, 51, 51)',
                zerolinecolor='rgb(51, 51, 51)',
            ),
            yaxis=go.layout.scene.YAxis(
                title="SAP_ID",
                tickfont=dict(size=10),
                ticktext=temp_sap,            # plot sap list as text (randomized list)
                tickvals=seq1,                      # plot numbers used to plot sap as scale
                tickwidth=6,
                tickmode='array',
                autorange=True,
                spikecolor='#AF28F3',
                spikethickness=4,
                backgroundcolor="#54F0BC",
                showbackground=True,
                gridcolor='rgb(51, 51, 51)',
                zerolinecolor='rgb(51, 51, 51)',
            ),
            zaxis=go.layout.scene.ZAxis(
                title="CGPA",
                tickfont=dict(size=13),
                # ticktext=cgpa,                     # plot cgpa list as text
                # tickvals=seq2,                     # sequence used to plot cgpa as scale
                nticks=10,
                tickmode="auto",
                tickwidth=6,
                spikecolor='#AF28F3',
                spikethickness=4,
                backgroundcolor="#54F0BC",
                showbackground=True,
                gridcolor='rgb(51, 51, 51)',
                zerolinecolor='rgb(51, 51, 51)',
            ),
            aspectratio=go.layout.scene.Aspectratio(
                x=4, y=4, z=2
            )
        ),
        paper_bgcolor='#54F0BC',
    )
    fig = go.Figure(data=data, layout=layout)
    # name_str = "3d-scatter-" + string_data + ".html"
    py.plot(fig, filename="3d-scatter.html")


def print_3ddata(dict_plot, temp, string_data, str1, str2):
    """Iterate through the given dictionary to produce useful data."""
    # for x in dict_plot:
    #     print(dict_plot[x][0], "  ", x , "  ", dict_plot[x][1])
    pattern = re.compile(r'[a-z]+(\s[a-z]{1}\.)?')
    names = []
    sap = []
    cgpa1 = []
    for val in dict_plot:
        sap.append(val)                                        # sap list
        na = pattern.match(dict_plot[val][0]).group(0)
        names.append(na)                                   # names list
        cgpa1.append(dict_plot[val][1])              # CGPA list

    # print(names, "  ", sap, "  ", len(cgpa))

    cgpa2 = []
    if temp is not None:
        for val in temp:
            cgpa2.append(temp[val][1])
    else:
        cgpa2 = None

    seq1 = [a for a in range(1, 59)]              # sequence for names

    # to randomize the sap (y axis)
    seq2 = []                                                   # sequence for sap
    temp_dict = {}
    i = 0
    while len(seq2) is not 58:
        r = random.randint(1, 58)
        if r not in seq2:
            seq2.append(r)
            temp_dict[r] = sap[i]
            i += 1

    # print(seq2, "  ", len(seq2), "   ", len(sap), "   ", temp_dict, "  ", len(temp_dict))

    # to sort the temp_dict on the key values
    temp_dict_1 = collections.OrderedDict(sorted(temp_dict.items()))

    temp_sap = []
    for val in temp_dict_1:
        temp_sap.append(temp_dict_1[val])

    # print(temp_dict_1, "  ", len(temp_dict_1), "  ", temp_sap)
    del(temp_dict)
    del(temp_dict_1)
    cgreen = '\033[92m'
    cend = '\033[0m'
    print(cgreen + "\n****Data has been plotted in the Scattered 3D graph format --[to see the graph open WEB BROWSER]****" + cend)
    plot_3dscattergraph(names, temp_sap, cgpa1, cgpa2, seq1, seq2, string_data, str1, str2)


def plot_2dscattergraph(sap, name, cgpa_list, sem_list):
    """Plot the 2D stattered graph by using WebGL application."""
    trace1 = go.Scatter(
        x=sem_list,
        y=cgpa_list,
        mode='lines+markers',
        marker=dict(
            size=16,
            color=cgpa_list,
            colorscale='Viridis',
        )
    )
    data = [trace1]
    layout = go.Layout(
        title="Graph of " + str(sap) + "  (" + name + ") :",
        font=dict(family='Playfair Display', size=14, color='black'),
        margin=go.layout.Margin(
            l=100,
            b=100,
        ),
        annotations=[
            dict(
                x="Sem III",
                y=cgpa_list[2],
                xref='x',
                yref='y',
                text='Predicted Value',
                showarrow=True,
                arrowhead=7,
                ax=0,
                ay=-40
            )],
        xaxis=dict(
            title='Semester',
            titlefont=dict(
                family='Playfair Display',
                size=20,
            ),
            ticklen=5,
            spikecolor='#AF28F3',
            spikethickness=2,
            zeroline=True,
            zerolinecolor='black',
            zerolinewidth=2,
            tickfont=dict(
                family='Playfair Display',
                size=14,
                color='black'
            ),
        ),
        yaxis=dict(
            title='CGPA',
            titlefont=dict(
                family='Playfair Display',
                size=20,
            ),
            ticklen=5,
            spikecolor='#AF28F3',
            spikethickness=2,
            zeroline=True,
            zerolinecolor='black',
            zerolinewidth=2,
            tickfont=dict(
                family='Playfair Display',
                size=14,
                color='black'
            ),
        ),
        showlegend=False,
        paper_bgcolor='#54F0BC',
        plot_bgcolor='#54F0BC',
    )
    fig = go.Figure(data=data, layout=layout)
    py.plot(fig, filename='2d-scatter.html')


def data_plot():
    os.system('color F')
    cblue = '\033[96m'
    cend = '\033[0m'
    """Extract data form pickle file."""               # data in the pickle file is stored as { sap:  [name, sem] }
    with open("Pickle_files/test1_data.pickle", "rb") as data_in:
        dict1 = pickle.load(data_in)
    with open("Pickle_files/test2_data.pickle", "rb") as data_in:
        dict2 = pickle.load(data_in)
    with open("Pickle_files/test3_data.pickle", "rb") as data_in:
        dict3 = pickle.load(data_in)

    while True:
        print(cblue + """
            1.Plot the Semester I result.
            2.Plot the Semester II result.
            3.Plot the Semester III result (Predicted Results).
            4.Compare the Semester I and II results.
            5.Compare the Semester II and III (Predicted) results.
            6.Enter any SAP_ID to compare their all three Semester results.
            7.Exit.""" + cend)
        try:
            ch = int(input(cblue + "Enter Your choice : " + cend))
            if ch is 1:
                print_3ddata(dict1, None, "Semester I", None, None)
            elif ch is 2:
                print_3ddata(dict2, None, "Semester II", None, None)
            elif ch is 3:
                print_3ddata(dict3, None, "Semester III (Predicted Results)", None, None)
            elif ch is 4:
                print_3ddata(dict1, dict2, "Comparison between Sem I & Sem II results", "Sem I", "Sem II")
            elif ch is 5:
                print_3ddata(dict2, dict3, "Comparison between Sem II & Sem III (Predicted) results", "Sem II", "Sem III")
            elif ch is 6:
                try:
                    sap = int(input(cblue + "Enter the SAP_ID : " + cend))
                    cgpa_data_list = [dict1[sap][1], dict2[sap][1], dict3[sap][1]]
                    sem_list = ["Sem I", "Sem II", "Sem III"]
                    cgreen = '\033[92m'
                    cend = '\033[0m'
                    print(cgreen + "\n****Data has been plotted in the Scattered 2D graph format --[to see the graph open WEB BROWSER]****" + cend)
                    plot_2dscattergraph(sap, dict1[sap][0], cgpa_data_list, sem_list)
                except Exception as event:
                    cred = '\033[91m'
                    cend = '\033[0m'
                    print(cred + "Error\n", str(event), "is not a valid SAP_ID!" + cend)
            else:
                break
        except Exception as event:
            cred = '\033[91m'
            cend = '\033[0m'
            print(cred + "Error\n", str(event), "is not a valid choice!" + cend)
