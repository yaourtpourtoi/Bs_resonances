from RooSpace import *
from DataExplorer import DataExplorer
import CMS_tdrStyle_lumi

from math import sqrt
import json
from numpy import array

CMS_tdrStyle_lumi.extraText = "Preliminary"
#
var_discr.setMin(left_discr_data); var_discr.setMax(right_discr_data); var_discr.setBins(nbins_discr_data)
PHI_mass_Cjp.setMin(left_phi_data); PHI_mass_Cjp.setMax(right_phi_data); PHI_mass_Cjp.setBins(nbins_phi_data)
var_control.setMin(left_control_data); var_control.setMax(right_control_data);  var_control.setBins(nbins_control_data)
#
file_data = ROOT.TFile('new_2_with_more_B0_e3de87.root')
data = ROOT.RooDataSet('data', '', file_data.Get('mytree'), ROOT.RooArgSet(var_discr, var_control, PIPI_mass_Cjp, PHI_mass_Cjp))
data = data.reduce(cuts_Bs_data + '&&' + cuts_phi_data + ' && ' + cuts_control_data + ' && ' + cuts_pipi[MODE])
#
chi2_results = {}

            #------------------#
            ##  fixing shape  ##
            #------------------#

w_Bs, f_Bs = get_workspace('workspace_' + MODE + '_Bs.root', 'workspace')
w_psi, f_psi = get_workspace('workspace_psi_control.root', 'workspace')
w_X, f_X = get_workspace('workspace_X_control.root', 'workspace')
w_phi, f_phi = get_workspace('workspace_' + MODE + '_phi.root', 'workspace')

###
w_delta_phi, f_delta_phi = get_workspace('workspace_' + MODE + '_delta_gen_phi_dRmatched_qM.root', 'workspace')
sigma_delta_1.setVal(w_delta_phi.var('sigma_delta_1').getVal());  sigma_delta_2.setVal(w_delta_phi.var('sigma_delta_2').getVal());
fr_delta.setVal(w_delta_phi.var('fr_delta').getVal()); # fr_Bs_1 = w_Bs.var('fr_Bs_1'); fr_Bs_2 = w_Bs.var('fr_Bs_2')
# mean_delta.setVal(w_delta_phi.var('mean_delta').getVal());

###
sigma_Bs_1.setVal(w_Bs.var('sigma_Bs_1').getVal());  sigma_Bs_2.setVal(w_Bs.var('sigma_Bs_2').getVal());
# sigma_Bs_3.setVal(w_Bs.var('sigma_Bs_3').getVal());
# sigma_Bs.setVal(w_Bs.var('sigma_Bs').getVal());
# gamma_BW_Bs.setVal(w_Bs.var('gamma_BW_Bs').getVal());
fr_Bs.setVal(w_Bs.var('fr_Bs').getVal());
# fr_Bs_1.setVal(w_Bs.var('fr_Bs_1').getVal()); fr_Bs_2.setVal(w_Bs.var('fr_Bs_2').getVal());
mean_Bs.setVal(w_Bs.var('mean_Bs').getVal());

###
sigmaCB_phi_1.setVal(w_phi.var('sigmaCB_phi_1').getVal()); alpha_phi_1.setVal(w_phi.var('alpha_phi_1').getVal()); n_phi_1.setVal(w_phi.var('n_phi_1').getVal())
sigmaCB_phi_2.setVal(w_phi.var('sigmaCB_phi_2').getVal()); alpha_phi_2.setVal(w_phi.var('alpha_phi_2').getVal()); n_phi_2.setVal(w_phi.var('n_phi_2').getVal())
fr_phi.setVal(w_phi.var('fr_phi').getVal());
# gamma_BW_phi.setVal(w_phi.var('gamma_BW_phi').getVal());
# sigma_gauss_phi.setVal(w_phi.var('sigma_gauss_phi').getVal());
# sigma_phi.setVal(w_phi.var('sigma_phi').getVal());
# mean_zero_phi.setVal(w_phi.var('mean_zero_phi').getVal());
mean_phi.setVal(w_phi.var('mean_phi').getVal());

###
sigma_psi_1.setVal(w_psi.var('sigma_psi_1').getVal()); sigma_psi_2.setVal(w_psi.var('sigma_psi_2').getVal());
# sigma_psi_3.setVal(w_psi.var('sigma_psi_3').getVal());
# sigma_psi.setVal(w_psi.var('sigma_psi').getVal());
# gamma_BW_psi.setVal(w_psi.var('gamma_BW_psi').getVal());
fr_psi.setVal(w_psi.var('fr_psi').getVal()); # fr_psi_1.setVal(w_psi.var('fr_psi_1').getVal()); fr_psi_2.setVal(w_psi.var('fr_psi_2').getVal());
mean_psi.setVal(w_psi.var('mean_psi').getVal());

###
sigma_X_1.setVal(w_X.var('sigma_X_1').getVal()); sigma_X_2.setVal(w_X.var('sigma_X_2').getVal());
# sigma_X_3.setVal(w_X.var('sigma_X_3').getVal());
# sigma_X.setVal(w_X.var('sigma_X').getVal());
# gamma_BW_X.setVal(w_X.var('gamma_BW_X').getVal());
fr_X.setVal(w_X.var('fr_X').getVal()); # fr_X_1.setVal(w_X.var('fr_X_1').getVal()); fr_X_2.setVal(w_X.var('fr_X_2').getVal());
mean_X.setVal(w_X.var('mean_X').getVal());

###########################################################################################################

sigma_Bs_1.setConstant(1); sigma_Bs_2.setConstant(1); sigma_Bs_3.setConstant(1);
sigma_Bs.setConstant(1); gamma_BW_Bs.setConstant(1);
fr_Bs.setConstant(1); fr_Bs_1.setConstant(1); fr_Bs_2.setConstant(1);

sigma_delta_1.setConstant(1); sigma_delta_2.setConstant(1); fr_delta.setConstant(1);
mean_delta.setVal(0.); mean_delta.setConstant(1)

sigmaCB_phi_1.setConstant(1); alpha_phi_1.setConstant(1); n_phi_1.setConstant(1);
sigmaCB_phi_2.setConstant(1); alpha_phi_2.setConstant(1); n_phi_2.setConstant(1);
gamma_BW_phi.setConstant(1); sigma_gauss_phi.setConstant(1); sigma_phi.setConstant(1)
fr_phi.setConstant(1); mean_zero_phi.setConstant(1)

sigma_psi_1.setConstant(1); sigma_psi_2.setConstant(1); sigma_psi_3.setConstant(1);
sigma_psi.setConstant(1); gamma_BW_psi.setConstant(1)
fr_psi.setConstant(1);  fr_psi_1.setConstant(1); fr_psi_2.setConstant(1)

sigma_X_1.setConstant(1); sigma_X_2.setConstant(1); sigma_X_3.setConstant(1);
sigma_X.setConstant(1); gamma_BW_X.setConstant(1)
fr_X.setConstant(1); fr_X_1.setConstant(1); fr_X_2.setConstant(1)

N_B0_refl.setVal(0.); N_B0_refl.setConstant(1)


            #---------------#
            ##  Inclusive  ##
            #---------------#

# file_out_data = open('/home/yaourt/Study/Bs_resonances/' + SPLOT_FROM + '->' + SPLOT_TO + '/' + MODE +'_data_evtN.txt', 'w')

DE_inclus = DataExplorer(name=SPLOT_CUT, var=var[SPLOT_CUT], data=data, model=model[SPLOT_CUT], is_extended=False, poi=N_sig[SPLOT_CUT])
DE_inclus.fit(is_sum_w2=False)
#
DE_inclus.set_regions()
data_sig, data_side = DE_inclus.get_regions()
#
c_inclus = ROOT.TCanvas("c_inclus", "c_inclus", 800, 600); CMS_tdrStyle_lumi.CMS_lumi(c_inclus, 2, 0);
frame_inclus = DE_inclus.plot_on_var();
chi2_results.update(DE_inclus.chi2_test())
#
frame_inclus_max = frame_inclus.GetMaximum(); coeffs = array([0.75, 0.85, 0.95]) if MODE == 'X' else array([0.5, 0.62, 0.75])
y_sdb_left, y_sr, y_sdb_right = frame_inclus_max*coeffs
frame_inclus = DE_inclus.plot_regions(frame_inclus, y_sdb_left, y_sr, y_sdb_right)
frame_inclus.Draw()
# c_inclus.Update(); c_inclus.RedrawAxis(); #c_inclus.GetFrame().Draw();
# c_inclus.SaveAs('~/Study/Bs_resonances/' + SPLOT_FROM + '->' + SPLOT_TO + '/c_inclus___' + MODE + refl_line + '.pdf')

            #-------------#
            ##  sPlot I  ##
            #-------------#

if REFL_ON and MODE == 'psi':  N_B0_refl.setVal(9.); N_B0_refl.setConstant(0)
else:        N_B0_refl.setVal(0.); N_B0_refl.setConstant(1)
if SPLOT_FROM == 'Bs' and MODE == 'X': mean[SPLOT_FROM].setConstant(1)

DE_1 = DataExplorer(name=SPLOT_FROM, var=var[SPLOT_FROM], data=data_sig, model=model[SPLOT_FROM], is_extended=False, poi=N_sig[SPLOT_FROM])
DE_1.fit(fix_float=a[SPLOT_FROM], is_sum_w2=False)
#
c_sPlot_1 = ROOT.TCanvas("c_sPlot_1", "c_sPlot_1", 800, 600); CMS_tdrStyle_lumi.CMS_lumi(c_sPlot_1, 2, 0);
frame_DE_1 = DE_1.plot_on_var()
chi2_results.update(DE_1.chi2_test())
frame_DE_1.Draw()

# c_sPlot_1.Update(); c_sPlot_1.RedrawAxis(); # c_sPlot_1.GetFrame().Draw();
# c_sPlot_1.SaveAs('~/Study/Bs_resonances/' + SPLOT_FROM + '->' + SPLOT_TO + '/c_sPlot_1_' + MODE + refl_line + '.pdf')

# file_out_data.write(str(N_sig[SPLOT_TO].getVal()) + ' ' + str(N_sig[SPLOT_TO].getError()) + '\n')

            #--------------#
            ##  sPlot II  ##
            #--------------#

sPlot_list = ROOT.RooArgList(N_sig[SPLOT_FROM], N_bkgr[SPLOT_FROM], N_B0_refl) if SPLOT_FROM == 'Bs' else ROOT.RooArgList(N_sig[SPLOT_FROM], N_bkgr[SPLOT_FROM])
sData_sig = ROOT.RooStats.SPlot('sData_sig', 'sData_sig', data_sig, model[SPLOT_FROM], sPlot_list)
data_sig_w = ROOT.RooDataSet(data_sig.GetName(), data_sig.GetTitle(), data_sig, data_sig.get(), '1 > 0', N_sig[SPLOT_FROM].GetName() + '_sw')
data_sig_w.SetName('sig_w')
hist_sig_weighted = ROOT.RooDataHist('hist_sig_weighted', 'hist_sig_weighted', ROOT.RooArgSet(var[SPLOT_TO]), data_sig_w) ### binning for this var was already previously set
#
mean_phi.setVal(1.01946); mean_phi.setConstant(1)
DE_2 = DataExplorer(name=SPLOT_TO, var=var[SPLOT_TO], data=hist_sig_weighted, model=model[SPLOT_TO], is_extended=False, poi = fr_model_phi)
DE_2.chi2_fit()

# fr_model_phi.setVal(0.); fr_model_phi.setConstant(1)
# DE_2.chi2_fit()
# df = DE_2.tnull_toys(n_toys = 40000, seed = 332, save=False)

c_sPlot_2 = ROOT.TCanvas("c_sPlot_2", "c_sPlot_2", 800, 600); CMS_tdrStyle_lumi.CMS_lumi(c_sPlot_2, 2, 0);
frame_DE_2 = DE_2.plot_on_var()
chi2_results.update(DE_2.chi2_test())
frame_DE_2.Draw()
# c_sPlot_2.Update(); c_sPlot_2.RedrawAxis(); # c_sPlot_2.GetFrame().Draw();
# c_sPlot_2.SaveAs('~/Study/Bs_resonances/' + SPLOT_FROM + '->' + SPLOT_TO + '/c_sPlot_1_' + MODE + refl_line + '.pdf')

#             #---------------#
#             ##  sPlot III  ##
#             #---------------#
#
# mean[SPLOT_FROM].setConstant(1)
# N_B0_refl.setVal(0.); N_B0_refl.setConstant(1)
#
# DE_3 = DataExplorer(name=SPLOT_FROM, var=var[SPLOT_FROM], data=data_side, model=model[SPLOT_FROM], is_extended=True, poi=N_sig[SPLOT_FROM])
# DE_3.fit(fix_float=a[SPLOT_FROM], is_sum_w2=False)
# #
# # w3 = DE_3.prepare_workspace(poi=N_sig[SPLOT_FROM], nuisances=a[SPLOT_FROM] + [mean[SPLOT_FROM], N_bkgr[SPLOT_FROM]])
# # asympt_rrr = DE_3.asympt_signif(w=w3)
# # asympt_rrr.Print()
# #
# c_sPlot_3 = ROOT.TCanvas("c_sPlot_3", "c_sPlot_3", 800, 600); CMS_tdrStyle_lumi.CMS_lumi(c_sPlot_3, 2, 0);
# frame_DE_3 = DE_3.plot_on_var()
# chi2_results.update(DE_3.chi2_test())
# frame_DE_3.Draw()
# # c_sPlot_3.Update(); c_sPlot_3.RedrawAxis(); # c_sPlot_3.GetFrame().Draw();
# # c_sPlot_3.SaveAs('~/Study/Bs_resonances/' + SPLOT_FROM + '->' + SPLOT_TO + '/c_sPlot_3_' + MODE + refl_line + '.pdf')
#
# # file_out_data.write(str(N_sig[SPLOT_FROM].getVal()) + ' ' + str(N_sig[SPLOT_FROM].getError()) + '\n')
#
#             #--------------#
#             ##  sPlot IV  ##
#             #--------------#
#
# mean[SPLOT_TO].setConstant(1)
#
# sData_side = ROOT.RooStats.SPlot('sData_side', 'sData_side', data_side, model[SPLOT_FROM], sPlot_list)
# data_side_w = ROOT.RooDataSet(data_side.GetName(), data_side.GetTitle(), data_side, data_side.get(), '1 > 0', N_sig[SPLOT_FROM].GetName() + '_sw')
# data_side_w.SetName('side_w')
# hist_side_weighted = ROOT.RooDataHist('hist_side_weighted', 'hist_side_weighted', ROOT.RooArgSet(var[SPLOT_TO]), data_side_w) ### binning for this var was already previously set
# #
# DE_4 = DataExplorer(name=SPLOT_TO, var=var[SPLOT_TO], data=hist_side_weighted, model=model[SPLOT_TO], is_extended=False, poi = fr_model_phi)
# DE_4.chi2_fit()
# # #
# # w4 = DE_4.prepare_workspace(poi = fr_model_phi, nuisances = a[SPLOT_TO] + [mean[SPLOT_TO]])
# # asympt_rrr = DE_4.asympt_signif(w = w4)
# # asympt_rrr.Print()
# # #
# c_sPlot_4 = ROOT.TCanvas("c_sPlot_4", "c_sPlot_4", 800, 600); CMS_tdrStyle_lumi.CMS_lumi(c_sPlot_4, 2, 0);
# frame_DE_4 = DE_4.plot_on_var()
# chi2_results.update(DE_4.chi2_test())
# frame_DE_4.Draw()
# # c_sPlot_4.Update(); c_sPlot_4.RedrawAxis(); # c_sPlot_4.GetFrame().Draw();
# # c_sPlot_4.SaveAs('~/Study/Bs_resonances/' + SPLOT_FROM + '->' + SPLOT_TO + '/c_sPlot_4_' + MODE + refl_line + '.pdf')

            #-------------#
            ##  Writing  ##
            #-------------#

# file_out_data.write(str(N_sig[SPLOT_TO].getVal()) + ' ' + str(N_sig[SPLOT_TO].getError()) + '\n')
# file_out_data.close()

# with open('./fit_validation/chis_' + MODE + '.txt', 'w') as file:
#     file.write(json.dumps(chi_dict))
