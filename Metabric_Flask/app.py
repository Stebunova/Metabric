import flask
from flask import render_template
import pickle
import sklearn
import numpy as np
from sklearn.preprocessing import OrdinalEncoder
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from sksurv.ensemble import RandomSurvivalForest
# print('Hello Metabric_flask')

app = flask.Flask(__name__, template_folder = "templates")

@app.route('/', methods = ['POST', 'GET'])

@app.route('/index', methods = ['POST', 'GET'])
def main():
    if flask.request.method =='GET':
        return render_template('main.html')
    
    if flask.request.method =='POST':
        with open('rsf_pkl.pkl', 'rb') as f:
            Metabric_model = pickle.load(f)

    age = float(flask.request.form['num__age_at_diagnosis'])
    ct = float(flask.request.form['num__chemotherapy'])
    hist = float(flask.request.form['num__neoplasm_histologic_grade'])
    ht = float(flask.request.form['num__hormone_therapy'])
    ln = float(flask.request.form['num__lymph_nodes_examined_positive'])
    mut = float(flask.request.form['num__mutation_count'])
    nott = float(flask.request.form['num__nottingham_prognostic_index'])
    rad = float(flask.request.form['num__radio_therapy'])
    siz = float(flask.request.form['num__tumor_size'])
    stag = float(flask.request.form['num__tumor_stage'])
    surg = float(flask.request.form['cat__type_of_breast_surgery'])
    typ = float(flask.request.form['cat__cancer_type_detailed'])
    cell = float(flask.request.form['cat__cellularity'])
    pam = float(flask.request.form['cat__pam50_+_claudin-low_subtype'])
    ihc = float(flask.request.form['cat__er_status_measured_by_ihc'])
    er = float(flask.request.form['cat__er_status'])
    snp = float(flask.request.form['cat__her2_status_measured_by_snp6'])
    her = float(flask.request.form['cat__her2_status'])
    oth = float(flask.request.form['cat__tumor_other_histologic_subtype'])
    men = float(flask.request.form['cat__inferred_menopausal_state'])
    clus = float(flask.request.form['cat__integrative_cluster'])
    lat = float(flask.request.form['cat__primary_tumor_laterality'])
    pr = float(flask.request.form['cat__pr_status'])
    clas = float(flask.request.form['cat__3-gene_classifier_subtype'])

    X = np.array([age, ct, hist, ht, ln, mut, nott, rad, siz, stag, surg, 
                typ, cell, pam, ihc, er, snp, 
                 her, oth, men, clus, lat, pr, clas]).reshape(1,-1)
    y_pred = Metabric_model.predict(X)
    return render_template('main.html', result = y_pred)

if __name__ == '__main__':
    app.run()
