from spartacus import load
import matplotlib.pyplot as plt
from matplotlib.figure import figaspect
import pandas as pd
import numpy as np

def plot_data_article(extracted_data,joint_to_plot, movement_to_plot = None):
    # list color is for each article
    list_color = ['#e41a1c','#377eb8','#4daf4a','#984ea3','#ff7f00','#e6ab02','#a65628','#f781bf','#999999','#1b9e77','#e7298a']
    # list marker is for each humeral motion

    list_marker = [".","p","*","+","D","s"]
    list_name_movement  = extracted_data.humeral_motion.unique()
    dict_marker = dict(zip(list_name_movement, list_marker))

    # slice of the extrated data
    data_to_plot = extracted_data.loc[extracted_data['joint'] == joint_to_plot]
    if movement_to_plot is not None:
        data_to_plot = data_to_plot.loc[data_to_plot['humeral_motion'] == movement_to_plot]
        name_figure = joint_to_plot+" "+movement_to_plot
    elif movement_to_plot is None:
        name_figure = joint_to_plot

    list_article = data_to_plot.article.unique()

    # Plot the data
    w, h = figaspect(0.2)
    fig, ax = plt.subplots(1,3, sharex=True, sharey='row', figsize=(w,h), squeeze=False)
    fig.suptitle(name_figure)
    for i, article in enumerate(list_article):
        # Currently too much data in these articles
        if article != "Kolz et al. 2020" and article != "Bourne 2003":
            data_to_plot_article = data_to_plot.loc[data_to_plot['article'] == article]
            list_humeral_motion = data_to_plot_article.humeral_motion.unique()
            ax[0, 2].plot([], [], marker='None', label=article, color=list_color[i])

            for j, humeral_motion in enumerate(list_humeral_motion):
                for ind_dof in range(3):
                    # Extract data of interest

                    data_to_plot_humeral_motion = data_to_plot_article.loc[data_to_plot_article['humeral_motion'] == humeral_motion ]
                    data_to_plot_humeral_motion = data_to_plot_humeral_motion.loc[data_to_plot_humeral_motion['degree_of_freedom'] == str(ind_dof+1)]

                    ax[0,ind_dof].plot(data_to_plot_humeral_motion['humerothoracic_angle'], data_to_plot_humeral_motion['value']*180/np.pi, color=list_color[i], marker=dict_marker[humeral_motion], linestyle='None')


    # Set the graph parameters
    for ind in range(3):
        ax[0,ind].set_ylim([-180, 180])
        ax[0,ind].set_xlim([0, 180])
        ax[0, ind].set_title('DoF' + str(ind + 1))
        ax[0,ind].set_xlabel("Humerothoracic angle (°)")

    ax[0, 0].set_ylabel("Angle (°)")
    #ax[0, 0].set_ylabel("Translation (mm)")


    if movement_to_plot is None:
        list_all_movement = data_to_plot.humeral_motion.unique()
        for name_movement in list_all_movement:
            ax[0, 2].plot([], [], label=name_movement, color='black', marker=dict_marker[name_movement], linestyle='None')

    ax[0,2].legend(bbox_to_anchor=(1.04, 1),loc='upper left')
    plt.subplots_adjust(top=0.8,bottom=0.2,right=0.7,wspace=0.1,hspace=0.1)
    plt.show()

if __name__ == "__main__":

    # extracted_data = load().import_confident_data()
    # extracted_data.angle_translation = "angle"
    extracted_data = pd.read_pickle("my_data.pkl")

    # Joint to plot
    # array(['scapulothoracic', 'glenohumeral', 'acromioclavicular',
    #       'sternoclavicular'], dtype=object)
    joint_to_plot = "scapulothoracic"

    # array(['frontal elevation', 'horizontal flexion', 'scapular elevation',
    #        'internal-external rotation 90 degree-abducted',
    #        'sagittal elevation',
    #        'internal-external rotation 0 degree-abducted'], dtype=object)
    movement_to_plot = 'frontal elevation'
    movement_to_plot = None

    plot_data_article(extracted_data,joint_to_plot, movement_to_plot)