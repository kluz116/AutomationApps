import json


def getMessage(res):
    results_json_str = res['responseValue'][0]['results']
    results_dict = json.loads(results_json_str)
    message = results_dict['Message']
    return message


def getbatchID(res):
    results_json_str = res['responseValue'][0]['results']
    results_dict = json.loads(results_json_str)
    trx_status_json_str = results_dict['TrxStatus']
    trx_status_dict = json.loads(trx_status_json_str)
    trx_batch_id = trx_status_dict['TrxBatchID']
    return trx_batch_id


def getSerialID(res):
    results_json_str = res['responseValue'][0]['results']
    results_dict = json.loads(results_json_str)
    trx_status_json_str = results_dict['TrxStatus']
    trx_status_dict = json.loads(trx_status_json_str)
    trx_Serial_id = trx_status_dict['SerialID']
    return trx_Serial_id