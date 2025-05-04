import streamlit as st
from sklearn.decomposition import PCA
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import os
from matplotlib import cm
from dotenv import load_dotenv

def load_openai_API(envpath='../resources/envfile.env'):
    ''' loads openai api and returns 
    Parameters
    ----------
    envpath:str,default='resources/envfile.env'
        path leading to the location of our api key environment file

    Returns
    -------
    None


    Notes
    -----
    This would have to be replaced from person to person typically but, i copied the env file into the directory so it holds 


    Examples
    --------

    '''
    load_dotenv(envpath)
    openai_api_key = os.getenv("OPENAI_API_KEY")
    print("KEY LOADED:", openai_api_key)
    return

def load_home_button(sessionstate):
    '''function for neater loading of the home button
    
    '''
    sessionstate=sessionstate if sessionstate is not None else st.session_state

    home_button = st.button("back_to_home")
    if home_button:
        st.session_state.page = None
        st.rerun()


def run_PCA(feature_matrix,n):

    pca=PCA(n_components=n)
    pca.fit(feature_matrix)
    X_pca = pca.transform(feature_matrix)
    weights = pca.components_
    explained_variance_ratio_ = pca.explained_variance_ratio_

    print("X_pca shape (new data):",X_pca.shape)
    print(f"the explained variance ratio is {explained_variance_ratio_}")
    print("weights shape:", weights.shape) 
    
    return X_pca,weights,explained_variance_ratio_

#Optimizing kmeans
def plot_sillohette_scores(cluster_range, silhouette_scores, outfile_path="sillohette_method.png"):
    '''quickly plot sillouhette scores afte running kmeans
    Parameters
    ----------

    Returns
    -------

    Notes
    -----


    Examples
    --------

    '''
    # Optimal k is where the silhouette score is highest

    optimal_k_sil = cluster_range[np.argmax(silhouette_scores)]#return index 

    # Plot Silhouette Scores
    plt.figure(figsize=(8, 5))
    plt.plot(cluster_range, silhouette_scores, marker='o', linestyle='-')
    plt.axvline(optimal_k_sil, color='red', linestyle='--', linewidth=2, label=f'Optimal k = {optimal_k_sil}')
    
    plt.xlabel('Number of Clusters (k)')
    plt.ylabel('Silhouette Score')
    plt.title('Silhouette Score for optimal K')
    plt.legend()
    plt.grid(True)
    plt.savefig(outfile_path+'sillohuette_plot', dpi=300)

    return optimal_k_sil
 
def plot_elbow_scores(cluster_range, inertia_scores, outfile_path="elbow_method.png"):
    '''quickly plot sillouhette scores afte running kmeans
    Parameters
    ----------

    Returns
    -------

    Notes
    -----


    Examples
    --------

    '''

    # Find the elbow point using the difference in inertia
    diff = np.diff(inertia_scores)  # First derivative
    diff2 = np.diff(diff)  # Second derivative (change in slope)
    optimal_k = cluster_range[np.argmin(diff2)+1]  # +1 because diff2 is one step shorter

    # Plot the Elbow Method
    plt.figure(figsize=(8, 5))
    plt.plot(cluster_range, inertia_scores, marker='o', linestyle='-')
    plt.axvline(optimal_k, color='red', linestyle='--', linewidth=2, label=f'Optimal k = {optimal_k}')

    plt.xlabel('Number of Clusters (k)')
    plt.ylabel('Inertia (Sum of Squared Distances)')
    plt.title('Elbow Method for Optimal k')
    plt.legend()
    plt.grid(True)

    plt.savefig(outfile_path+'elbow_plot', dpi=300)  # Save the figure


    return optimal_k


# credit here to Jennifer Rose QAC 380 Ai Tools for data analysis
def preform_clust_opt(data,outfile_path, max_clusters=10):
    '''
    Parameters
    ----------
    data:np.ndarray,shape=(n_sample,n_features),
        A feature matrix of any kind, hopefully one provided from the rest of the pipeline but in theory, this is 
        just a scikit learn wrapper so you can plug anything you want really

    Returns
    ----------
    optimal_k_silhouette_labels:listlike,shape=(n_sameples,)
        A list of labels pertaining to the number of initial centroids for K-Means that it was decided that
        was appropriate via-silhouette score evalation 
    
    optimal_k_elbow_labels:listlike,shape=(n_sameples,)
        A list of labels pertaining to the number of initial centroids for K-Means that it was decided that
        was appropriate via-silhouette score evalation 
    
    Notes
    ----------
    Not much to say other than we try and optimize the clusters based on siollouhette scores and elbow plots of the data
    Honestly its kind of useful that I did this in this way because it opened up for me the concept of the problem with sillohuette scores
    in evaluating cluster quality found here:

    https://medium.com/biased-algorithms/silhouette-score-d85235e7638b

    
    Examples
    ----------
    
    '''
    #keepinig track of our scores 
    inertia_scores,all_labels = [],[]
    cluster_range = range(2, max_clusters+2)

    for k in cluster_range:
        kmeans = KMeans(n_clusters=k, init='random', n_init=k, random_state=0) #we set
        kmeans.fit(data) #fit data and now we have everything transformed
        cluster_centers, inertia, cluster_labels = kmeans.cluster_centers_,kmeans.inertia_,kmeans.labels_

        inertia_scores.append(inertia)
        all_labels.append(cluster_labels)

        np.save(f"{outfile_path}kluster_labels_{k}clust",cluster_labels)
    

    optimal_elbow=plot_elbow_scores(cluster_range,inertia_scores,outfile_path)
    
    print(f'\nsize of labels:{len(all_labels)} ,optimal_elbow: {optimal_elbow}')
    
    # Now you can return optimal k values
    optimal_k_elbow_labels = all_labels[optimal_elbow-2] 
    
    return optimal_k_elbow_labels


def preform_clust(data, max_clusters=10):
    ''' this needs to be recommented as well

    Parameters
    ----------
    data:np.ndarray,shape=(n_sample,n_features),
        A feature matrix of any kind, hopefully one provided from the rest of the pipeline but in theory, this is 
        just a scikit learn wrapper so you can plug anything you want really

    Returns
    ----------
    optimal_k_silhouette_labels:listlike,shape=(n_sameples,)
        A list of labels pertaining to the number of initial centroids for K-Means that it was decided that
        was appropriate via-silhouette score evalation 
    
    optimal_k_elbow_labels:listlike,shape=(n_sameples,)
        A list of labels pertaining to the number of initial centroids for K-Means that it was decided that
        was appropriate via-silhouette score evalation 
    
    Notes
    -----
    Not much to say other than we try and optimize the clusters based on siollouhette scores and elbow plots of the data
    Honestly its kind of useful that I did this in this way because it opened up for me the concept of the problem with sillohuette scores
    in evaluating cluster quality found here:

    https://medium.com/biased-algorithms/silhouette-score-d85235e7638b

    

    Examples
    --------


    
    '''

    kmeans = KMeans(n_clusters=max_clusters, init='random', random_state=0) #we set
    kmeans.fit(data) #fit data and now we have everything transformed
    cluster_centers, inertia, cluster_labels = kmeans.cluster_centers_,kmeans.inertia_,kmeans.labels_
    
    return cluster_labels


def visualize_traj_PCA_onepanel(X_pca, color_mappings, clustering=False, 
                                savepath=os.getcwd(), 
                                title="Principal Component Analysis (PCA) of GCU and CGU Systems", 
                                colors_list=['purple', 'orange', 'green', 'yellow', 'blue', 'red', 'pink', 'cyan', 'grey','brown'],
                                legend_labels = {'GCU Short': 'purple','GCU Long (0-80)': 'orange','GCU Long (80-160)': 'green','CGU Short': 'yellow','CGU Long (0-80)': 'blue','CGU Long (80-160)': 'red'}):
    
    ''' Visualizes data from an original feature matrix on two principal components after PCA

    Parameters
    ----------
    X_pca : np.ndarray, shape=(n_samples, n_components)
        The results of fitting a PCA analysis and using the .transform() method.

    color_mappings : list-like, shape=(n_samples)
        A list used to assign a color to each sample based on some mapping.
        If clustering=False, this should be a numeric array that will be mapped to a colormap.

    legend_labels : dict or None, default={'GCU Short': 'purple','GCU Long (0-80)': 'orange','GCU Long (80-160)': 'green','CGU Short': 'yellow','CGU Long (0-80)': 'blue','CGU Long (80-160)': 'red'}
        A dictionary mapping cluster labels to colors. If None, no legend is shown.

    clustering : bool, default=True
        If True, uses discrete colors from `colors_list`. If False, uses a colormap with a colorbar.

    savepath : str, default=current directory
        The full path where the output file will be saved.

    colors_list : list-like
        A list of colors to visualize discrete clusters.
    '''
    labels_font_dict = {
        'family': 'monospace',
        'size': 20,
        'weight': 'bold',
        'style': 'italic',
        'color': 'black',
    }

    fig = plt.figure(figsize=(16, 12), dpi=300)
    ax = plt.gca()

    unique_vals = np.unique(color_mappings)

    if clustering:
        # Define the legend mapping
        legend_labels = {
            'GCU Short': 'purple',
            'GCU Long (0-80)': 'orange',
            'GCU Long (80-160)': 'green',
            'CGU Short': 'yellow',
            'CGU Long (0-80)': 'blue',
            'CGU Long (80-160)': 'red'
        }

        scatter = ax.scatter(X_pca[:, 0], X_pca[:, 1], c=color_mappings, 
                             cmap=ListedColormap(colors_list[:len(unique_vals)]), alpha=0.6)

        if legend_labels is not None:
            ax.legend(prop={'size': 20, 'weight': 'bold'})
            legend_handles = [plt.Line2D([0], [0], marker='o', color='w', markersize=10, 
                                         markerfacecolor=color, label=label) 
                              for label, color in legend_labels.items()]
            ax.legend(handles=legend_handles, title="System Types", loc="upper right")
            

    else:
        from matplotlib.colors import BoundaryNorm
        # Use discrete colormap even in non-clustering mode
        discrete_cmap = ListedColormap(colors_list[:len(unique_vals)])
        boundaries = np.arange(min(unique_vals) - 0.5, max(unique_vals) + 1.5, 1)
        norm = BoundaryNorm(boundaries, discrete_cmap.N)

        scatter = ax.scatter(X_pca[:, 0], X_pca[:, 1], c=color_mappings, cmap=discrete_cmap, norm=norm, alpha=0.6)

        cbar = plt.colorbar(cm.ScalarMappable(norm=norm, cmap=discrete_cmap), ax=ax,
                            ticks=unique_vals, shrink=0.8, aspect=30, pad=0.02)
        cbar.set_label(label="Cluster Assignment", fontdict=labels_font_dict, rotation=270, labelpad=25)
        cbar.ax.yaxis.set_tick_params(color='white', labelsize=8)
        cbar.ax.set_yticklabels([str(int(val)) for val in unique_vals])

        for spine in ax.spines.values():
            spine.set_visible(False)

    ax.set_title(title, fontdict=labels_font_dict)
    ax.set_xlabel("Principal Component 1", fontdict=labels_font_dict)
    ax.set_ylabel("Principal Component 2", fontdict=labels_font_dict)
    ax.tick_params(axis='x', colors='black')  
    ax.tick_params(axis='y', colors='black')

    plt.tight_layout()
    plt.savefig(savepath, dpi=300)
    plt.close()