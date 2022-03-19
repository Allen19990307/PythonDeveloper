import json
from my_encoder import MyEncoder
f = open('data/python12345.txt','rb')
data1 = f.read()

f = open('data/text.txt','rb')
data2 = f.read()

# test案例
data = {
        "d": {
                "results": [{
                        "__metadata": {
                                "type": "dashboard_bwp.dashboard.MATERIALType",
                                "uri": "http://10.80.10.62:8000/dashboard_bwp/dashboard.xsodata/MATERIAL('52018087086825001')"
                        },
                        "ID": "52018087086825001"
                        }]
                        }
}

# dumps:把字典转换为json字符串
s = json.dumps(data2,cls=MyEncoder)
# print(s)

print(" -----------------------------")
# loads:把json转换为dict,
s1 = json.loads(s)

loads = json.loads(s1)
results_ = loads["d"]["results"]

# findindex = lambda self,i,value:sorted(self,key=lambda x:x[i]!=value)[0]

# print(findindex(results_,0,'uri'))

print(results_)


# print(s1)
# 打印statusCode对应的值
# print(s1[12])


"""
create table if not exists dwd_hana.hana(
 id                  string,                                 
 material            string,                       
 material_desc       string,                       
 id                  string,                       
 material            string,                       
 material_desc       string,                       
 prod_hier           string,                       
 prod_hier_desc      string,                       
 matl_type           string,                       
 matl_type_desc      string,                        
 prodh1              string,                        
 prodh1_desc         string,                        
 prodh2              string,                        
 prodh2_desc         string,                        
 prodh3              string,                        
 prodh3_desc         string,                        
 prodh4              string,                        
 prodh4_desc         string,                        
 prodh5              string,                        
 prodh5_desc         string,                        
 prodh6              string,                        
 prodh6_desc         string,                        
 prodh7              string,                        
 prodh7_desc         string,                        
 prodh8              string,                        
 prodh8_desc         string,                        
 prodh9              string,                        
 prodh9_desc         string,                        
 matl_group          string,                        
 matl_group_desc     string,                        
 matl_grp_1          string,                        
 matl_grp_2          string,                        
 matl_grp_3          string,                        
 matl_grp_4          string,                        
 matl_grp_5_desc     string,                        
 matl_grp_5          string,                        
 zmmplb              string,                        
 zmmplb_desc         string,                        
 zmmfs               string,                        
 zmmfs_desc          string,                        
 zmmwldj             string,                        
 prodh1_desc_h       string,                        
 prodh2_desc_h       string,                        
 prodh3_desc_h       string,                        
 prodh4_desc_h       string,                        
 prodh5_desc_h       string,                        
 prodh6_desc_h       string,                        
 prodh7_desc_h       string,                        
 prodh8_desc_h       string,                        
 prodh9_desc_h       string,                        
 prodh1_desc_s       string,                        
 prodh2_desc_s       string,                        
 prodh3_desc_s       string,                        
 prodh4_desc_s       string,                        
 prodh5_desc_s       string,                        
 prodh6_desc_s       string,                        
 prodh7_desc_s       string,                        
 prodh8_desc_s       string,                        
 prodh9_desc_s       string,                        
 zwq_ggfz            string,                        
 zwq_ggfz_desc       string,                        
 prodh3_px           string,                        
 zwq_zdpx            string,                        
 zwq_zdpx_desc       string,                        
 zwq_ggfz_lang       string,                        
 net_weight          string,                        
 gross_wt            string,                        
 mat09               string,                        
 mat09_desc          string,                        
 zmat5_fl2           string,                        
 mat07               string,                        
 mat07_desc          string,                        
 mat08               string,                        
 mat08_desc          string,                        
 mat06               string,                        
 mat06_desc          string,                        
 matl_grp_4_desc     string,                        
 material_sequence   string,                        
 zdpx                string,                        
 zdpx_desc           string,                        
 fzdpx               string,                        
 fzdpx_desc          string,                        
 only_mat            string,                        
 only_mat_descl      string,                        
 flag                string,                        
 listing_date        string,                        
 delisting_date      string
)



"""



