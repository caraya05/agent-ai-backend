import datetime

from django.db.models import Q
from django.utils import timezone

from companies.models import Company
from predictions.models import DataHistory, Prediction, Var


# Metodo para obtener tabla del dahsboard con items de bloqueados
# def get_data_all_companies(date_init: str, date_end: str):  # pylint: disable=R0914 R0912 R0915
#     data_table = []
#     # companies = Company.objects.exclude(is_staff=True, is_superuser=True).filter(id__in=[115, 102])
#     all_vars = Var.objects.filter(active=True).all()
#     companies = Company.objects.exclude(Q(is_staff=True) | Q(is_superuser=True) | Q(is_user=True))
#     for company in companies:  # pylint: disable=R1702
#         all_data_vars_ = [0, 0, 0]
#         all_data_vars_filter = [0, 0, 0]
#
#         filtered_data = DataHistory.objects.filter(company=company
#                                                    ).order_by("-date")
#         filtered_predictions = Prediction.objects.filter(company=company
#                                                          ).order_by("-date")
#         for i in filtered_data:
#             all_data_vars_[0] += len(i.vars)
#             for j in i.vars:
#                 if j["value"] != "":
#                     all_data_vars_[1] += 1
#         if all_data_vars_[0] > 0:
#             all_data_vars_[2] = round((all_data_vars_[1] / (filtered_data.count() * all_vars.count())) * 100, 2)
#
#         else:
#             all_data_vars_[2] = 0.0
#
#         if date_init and date_end:
#             filtered_data_ = DataHistory.objects.filter(company=company,
#                                                         date__lte=date_end,
#                                                         date__gte=date_init
#                                                         ).order_by("-date")
#             filtered_predictions_ = Prediction.objects.filter(company=company,
#                                                               date__lte=date_end,
#                                                               date__gte=date_init
#                                                               ).order_by("-date")
#             if filtered_data_.count() > 0:
#                 for i in filtered_data_:
#                     all_data_vars_filter[0] += len(i.vars)
#                     for j in i.vars:
#                         if j["value"] != "":
#                             all_data_vars_filter[1] += 1
#             if all_data_vars_[0] > 0 or all_data_vars_filter[1] > 0:
#                 all_data_vars_filter[2] = round(
#                     (all_data_vars_filter[1] / (filtered_data_.count() * all_vars.count())) * 100, 2)
#             else:
#                 all_data_vars_filter[2] = 0.0
#         data_company = dict(id=company.id,
#                             name_company=company.name_company,
#                             last_month_charge_data="",
#                             number_data_history_full=0,
#                             number_total_data_history_last_months=0.0,
#                             number_total_data_history=all_data_vars_[2] if not date_init and not date_end else
#                             all_data_vars_filter[2],
#                             number_prediction_month_current=filtered_predictions.filter(
#                                 date__month=timezone.now().month).count(),
#                             number_prediction_interval=filtered_predictions.count() if not date_init and not date_end
#                             else filtered_predictions_.count(),
#                             number_total_accidents=0,
#                             number_total_incidents=0,
#                             percentage_medium_physical_danger=0,
#                             percentage_medium_chemical_danger=0,
#                             percentage_medium_biological_danger=0,
#                             percentage_medium_biomechanical_danger=0,
#                             percentage_medium_conditions_danger=0, )
#         try:
#             date_current = timezone.now().date()
#             date_last_month = date_current - timezone.timedelta(days=36 * 31)
#             # print("cantidad de datos", filtered_data.filter(date__lte=date_current,
#             #                                                 date__gte=date_last_month).count())
#             for data_history in filtered_data:
#                 count_data_ok = []
#                 for var in data_history.vars:
#                     if var.get("value") != "":
#                         count_data_ok.append(var.get("value"))
#                         date_current = timezone.now().date()
#                         date_last_month = date_current - timezone.timedelta(days=36 * 30)
#                         # print(date_last_month, data_history.date, date_current)
#                         if date_last_month <= data_history.date <= date_current:
#                             # print("entro")
#                             data_company["number_total_data_history_last_months"] += 1
#                 if len(count_data_ok) == len(data_history.vars):
#                     if not data_company["last_month_charge_data"]:
#                         data_company["last_month_charge_data"] = data_history.date
#             data_company["number_total_data_history_last_months"] = round(
#                 (data_company["number_total_data_history_last_months"] / (36 * all_vars.count())) * 100, 2)
#             if date_init and date_end:
#                 filtered_data = filtered_data_
#
#             numbers_percent = {
#                 "pR1": 0,
#                 "pR2": 0,
#                 "pR3": 0,
#                 "pR4": 0,
#                 "pR5": 0,
#             }
#             for data_history in filtered_data:
#                 count_data_ok = []
#                 for var in data_history.vars:
#                     if var.get("name") == "pR1":
#                         data_company["percentage_medium_physical_danger"] += float(var.get("value")) \
#                             if var.get("value") != "" \
#                             else 0
#                         numbers_percent["pR1"] += 1 \
#                             if var.get("value") != "" \
#                             else 0
#                     if var.get("name") == "pR2":
#                         data_company["percentage_medium_chemical_danger"] += float(var.get("value")) \
#                             if var.get("value") != "" \
#                             else 0
#                         numbers_percent["pR2"] += 1 \
#                             if var.get("value") != "" \
#                             else 0
#                     if var.get("name") == "pR3":
#                         data_company["percentage_medium_biological_danger"] += float(var.get("value")) \
#                             if var.get("value") != "" \
#                             else 0
#                         numbers_percent["pR3"] += 1 \
#                             if var.get("value") != "" \
#                             else 0
#                     if var.get("name") == "pR4":
#                         data_company["percentage_medium_biomechanical_danger"] += float(var.get("value")) \
#                             if var.get("value") != "" \
#                             else 0
#                         numbers_percent["pR4"] += 1 \
#                             if var.get("value") != "" \
#                             else 0
#                     if var.get("name") == "pR5":
#                         data_company["percentage_medium_conditions_danger"] += float(var.get("value")) \
#                             if var.get("value") != "" \
#                             else 0
#                         numbers_percent["pR5"] += 1 \
#                             if var.get("value") != "" \
#                             else 0
#                     if var.get("name") == "nAccidentes":
#                         data_company["number_total_accidents"] += int(var.get("value")) \
#                             if var.get("value") != "" \
#                             else 0
#                     if var.get("name") == "nIncidentes":
#                         data_company["number_total_incidents"] += int(var.get("value")) \
#                             if var.get("value") != "" \
#                             else 0
#                     if var.get("value") != "":
#                         count_data_ok.append(var.get("value"))
#                 if len(count_data_ok) != 0:
#                     data_company["number_data_history_full"] += 1
#             if data_company["number_total_accidents"] > data_company["number_total_incidents"]:
#                 data_company["number_total_incidents"] += data_company["number_total_accidents"]
#             data_company["percentage_medium_physical_danger"] = round(
#                 data_company["percentage_medium_physical_danger"] / numbers_percent["pR1"], 2) \
#                 if numbers_percent["pR1"] > 0 \
#                 else 0
#             data_company["percentage_medium_chemical_danger"] = round(
#                 data_company["percentage_medium_chemical_danger"] / numbers_percent["pR2"], 2) \
#                 if numbers_percent["pR2"] > 0 \
#                 else 0
#             data_company["percentage_medium_biological_danger"] = round(
#                 data_company["percentage_medium_biological_danger"] / numbers_percent["pR3"], 2) \
#                 if numbers_percent["pR3"] > 0 \
#                 else 0
#             data_company["percentage_medium_biomechanical_danger"] = round(
#                 data_company["percentage_medium_biomechanical_danger"] / numbers_percent["pR4"],
#                 2) \
#                 if numbers_percent["pR4"] > 0 \
#                 else 0
#             data_company["percentage_medium_conditions_danger"] = round(
#                 data_company["percentage_medium_conditions_danger"] / numbers_percent["pR5"], 2) \
#                 if numbers_percent["pR5"] > 0 \
#                 else 0
#             data_table.append(data_company)
#         except Exception as ex:  # pylint: disable=W0703
#             print("error: ", ex)
#     data_table = sorted(data_table, key=lambda index: index['number_data_history_full'], reverse=True)
#     return data_table

def get_data_all_companies(date_init: str, date_end: str):  # pylint: disable=R0914 R0912 R0915
    data_table = []
    # companies = Company.objects.exclude(is_staff=True, is_superuser=True).filter(id__in=[102])
    all_vars = Var.objects.filter(active=True).all()
    companies = Company.objects.exclude(Q(is_staff=True) | Q(is_superuser=True) | Q(is_user=True))
    for company in companies:  # pylint: disable=R1702
        all_data_vars_ = [0, 0, 0]
        if date_init and date_end:
            filtered_data = DataHistory.objects.filter(company=company,
                                                       date__lte=date_end,
                                                       date__gte=date_init
                                                       ).order_by("-date")
            filtered_predictions = Prediction.objects.filter(company=company,
                                                             date__lte=date_end,
                                                             date__gte=date_init
                                                             ).order_by("-date")
        else:
            filtered_data = DataHistory.objects.filter(company=company
                                                       ).order_by("-date")
            filtered_predictions = Prediction.objects.filter(company=company
                                                             ).order_by("-date")
        for i in filtered_data:
            all_data_vars_[0] += len(i.vars)
            for j in i.vars:
                if j["value"] != "":
                    all_data_vars_[1] += 1
        if all_data_vars_[0] > 0:
            all_data_vars_[2] = round((all_data_vars_[1] / (filtered_data.count() * all_vars.count())) * 100, 2)
        else:
            all_data_vars_[2] = 0.0

        data_company = dict(id=company.id,
                            name_company=company.name_company,
                            last_month_charge_data="",
                            number_data_history_full=0,
                            number_total_data_history_last_months=0.0,
                            number_total_data_history=all_data_vars_[2],
                            number_prediction_month_current=filtered_predictions.filter(
                                date__month=timezone.now().month).count(),
                            number_prediction_interval=filtered_predictions.count(),
                            number_total_accidents=0,
                            number_total_incidents=0,
                            percentage_medium_physical_danger=0,
                            percentage_medium_chemical_danger=0,
                            percentage_medium_biological_danger=0,
                            percentage_medium_biomechanical_danger=0,
                            percentage_medium_conditions_danger=0, )
        try:
            for data_history in filtered_data:
                count_data_ok = []
                for var in data_history.vars:
                    if var.get("value") != "":
                        count_data_ok.append(var.get("value"))
                        date_current = timezone.now().date()
                        date_current = date_current.replace(day=30)
                        date_last_month = date_current - timezone.timedelta(days=36 * 30)
                        date_last_month = date_last_month.replace(day=1)
                        if date_last_month <= data_history.date <= date_current:
                            data_company["number_total_data_history_last_months"] += 1
                if len(count_data_ok) == len(data_history.vars):
                    if not data_company["last_month_charge_data"]:
                        data_company["last_month_charge_data"] = data_history.date
            data_company["number_total_data_history_last_months"] = round(
                (data_company["number_total_data_history_last_months"] / (36 * all_vars.count())) * 100, 2)

            numbers_percent = {
                "pR1": count_vars_in_data(filtered_data, "pR1"),
                "pR2": count_vars_in_data(filtered_data, "pR2"),
                "pR3": count_vars_in_data(filtered_data, "pR3"),
                "pR4": count_vars_in_data(filtered_data, "pR4"),
                "pR5": count_vars_in_data(filtered_data, "pR5")
            }

            data_company["percentage_medium_physical_danger"] = count_data_array(filtered_data, "pR1")
            data_company["percentage_medium_chemical_danger"] = count_data_array(filtered_data, "pR2")
            data_company["percentage_medium_biological_danger"] = count_data_array(filtered_data, "pR3")
            data_company["percentage_medium_biomechanical_danger"] = count_data_array(filtered_data, "pR4")
            data_company["percentage_medium_conditions_danger"] = count_data_array(filtered_data, "pR5")
            data_company["number_total_accidents"] = count_data_array(filtered_data, "nAccidentes")
            data_company["number_total_incidents"] = count_data_array(filtered_data, "nIncidentes")
            data_company["number_data_history_full"] = count_data_full(filtered_data)

            if data_company["number_total_accidents"] > data_company["number_total_incidents"]:
                data_company["number_total_incidents"] += data_company["number_total_accidents"]
            data_company["percentage_medium_physical_danger"] = round(
                data_company["percentage_medium_physical_danger"] / numbers_percent["pR1"], 2) \
                if numbers_percent["pR1"] > 0 \
                else 0
            data_company["percentage_medium_chemical_danger"] = round(
                data_company["percentage_medium_chemical_danger"] / numbers_percent["pR2"], 2) \
                if numbers_percent["pR2"] > 0 \
                else 0
            data_company["percentage_medium_biological_danger"] = round(
                data_company["percentage_medium_biological_danger"] / numbers_percent["pR3"], 2) \
                if numbers_percent["pR3"] > 0 \
                else 0
            data_company["percentage_medium_biomechanical_danger"] = round(
                data_company["percentage_medium_biomechanical_danger"] / numbers_percent["pR4"],
                2) \
                if numbers_percent["pR4"] > 0 \
                else 0
            data_company["percentage_medium_conditions_danger"] = round(
                data_company["percentage_medium_conditions_danger"] / numbers_percent["pR5"], 2) \
                if numbers_percent["pR5"] > 0 \
                else 0
            data_table.append(data_company)
        except Exception as ex:  # pylint: disable=W0703
            print("error: ", ex)
    data_table = sorted(data_table, key=lambda index: index['number_data_history_full'], reverse=True)
    return data_table


def count_data_array(array: [], name_array: str):
    count_data = 0
    for data_history in array:
        for var in data_history.vars:
            if var.get("name") == name_array:
                count_data += float(var.get("value")) \
                    if var.get("value") != "" \
                    else 0
    return count_data


def count_vars_in_data(array: [], name: str):
    count_data = 0
    for data_history in array:
        for var in data_history.vars:
            if var.get("name") == name:
                count_data += 1 \
                    if var.get("value") != "" \
                    else 0
    return count_data


def count_data_full(array: []):
    count_data = 0
    for data_history in array:
        count_data_ok = []
        for var in data_history.vars:
            if var.get("value") != "":
                count_data_ok.append(var.get("value"))
        if len(count_data_ok) != 0:
            count_data += 1
    return count_data
