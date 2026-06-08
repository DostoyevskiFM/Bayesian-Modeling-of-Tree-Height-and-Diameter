import pandas as pd
import arviz as az
import bambi as bmb

df = pd.read_csv('/Users/fiodarzianiutsich/Desktop/projekt/data_cleaning/red_spruce_2022.csv')

model_giant = bmb.Model("log_height ~ log_diameter + (1 | county) + (1 | county:plot_number)", df)
results_giant = model_giant.fit(target_accept=0.99, idata_kwargs={"log_likelihood": True})

model_county = bmb.Model('log_height ~ log_diameter + (log_diameter | county)', df)
results_county = model_county.fit(target_accept=0.99, idata_kwargs={"log_likelihood": True})

model_naive = bmb.Model("log_height ~ log_diameter", df)
results_naive = model_naive.fit(idata_kwargs={"log_likelihood": True})

model_str_prior = bmb.Model("log_height ~ log_diameter + (1 | county) + (1 | county:plot_number)",
                            data=df, priors={"log_diameter": bmb.Prior("Normal", mu=0.6, sigma=0.07)})
results_str_prior = model_str_prior.fit(target_accept=0.99, idata_kwargs={"log_likelihood": True})

dict_of_models = {"Giant": results_giant, "County": results_county, "Naive": results_naive, "Custom_prior": results_str_prior}

print(az.compare(dict_of_models))