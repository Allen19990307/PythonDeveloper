s1 =['qm_scrm_campaign                        ',
'qm_scrm_campaigncenter_luckydraw',
'qm_scrm_campaigncenter_meeting',
'qm_scrm_campaigncenter_promotion',
'qm_scrm_member_merge_history',
'qm_scrm_score_history',
'qm_scrm_static_group',
'qm_scrm_member_vip_level',
'qm_scrm_member_level_history',
'qm_scrm_member_protection_period_score',
'qm_scrm_member_growth_history',
'qm_scrm_member_privilege_reward',
'qm_scrm_member_score_setting',
'qm_scrm_member_task',
'qm_scrm_member_task_record',
'qm_scrm_member_task_reward',
'qm_scrm_member_score_limit',
'qm_scrm_member_event',
'qm_scrm_coupon',
'qm_scrm_coupon_endpoint',
'qm_scrm_ec_enter_store_welfare',
'qm_scrm_ec_product',
'qm_scrm_ec_present_campaign',
'qm_scrm_ec_flash_sale_campaign',
'qm_scrm_ec_groupon_campaign',
'qm_scrm_ec_groupon_record',
'qm_scrm_ec_product_comment',
'qm_scrm_ec_comment_recommend',
'qm_scrm_ec_discount_campaign',
'qm_scrm_ec_package_campaign',
'qm_scrm_ec_enter_store_welfare_accessed_record',
'qm_scrm_product',
'qm_scrm_product_classification                ',
'qm_scrm_product_category',
'qm_scrm_eccampaign_period_buy',
'qm_scrm_eccampaign_period_buy_delivery_plan',
'qm_scrm_eccampaign_bargain',
'qm_scrm_eccampaign_trial',
'qm_scrm_channel',
'qm_scrm_campaign_member',
'qm_scrm_campaign_log',
'qm_scrm_campaigncenter_campaign_reward_log',
'qm_scrm_campaigncenter_luckydraw_extra_chance',
'qm_scrm_campaigncenter_luckydraw_log',
'qm_scrm_campaign_survey_log',
'qm_scrm_campaigncenter_meeting_participant',
'qm_scrm_member'
]
s2 = [
'qm_scrm_campaign',
'qm_scrm_campaigncenter_luckydraw',
'qm_scrm_campaigncenter_meeting',
'qm_scrm_campaigncenter_promotion',
'qm_scrm_member_merge_history',
'qm_scrm_score_history',
'qm_scrm_static_group',
'qm_scrm_member_vip_level',
'qm_scrm_member_level_history',
'qm_scrm_member_protection_period_score',
'qm_scrm_member_growth_history',
'qm_scrm_member_privilege_reward',
'qm_scrm_member_score_setting',
'qm_scrm_member_task',
'qm_scrm_member_task_record',
'qm_scrm_member_task_reward',
'qm_scrm_member_score_limit',
'qm_scrm_member_event',
'qm_scrm_coupon',
'qm_scrm_coupon_endpoint',
'qm_scrm_ec_enter_store_welfare',
'qm_scrm_ec_product',
'qm_scrm_ec_present_campaign',
'qm_scrm_ec_flash_sale_campaign',
'qm_scrm_ec_groupon_campaign',
'qm_scrm_ec_groupon_record',
'qm_scrm_ec_product_comment',
'qm_scrm_ec_comment_recommend',
'qm_scrm_ec_discount_campaign',
'qm_scrm_ec_package_campaign',
'qm_scrm_ec_enter_store_welfare_accessed_record',
'qm_scrm_product',
'qm_scrm_product_classification                ',
'qm_scrm_product_category',
'qm_scrm_eccampaign_period_buy',
'qm_scrm_eccampaign_period_buy_delivery_plan',
'qm_scrm_eccampaign_bargain',
'qm_scrm_eccampaign_trial',
'qm_scrm_channel',
'qm_scrm_campaign_member',
'qm_scrm_campaign_log',
'qm_scrm_campaigncenter_campaign_reward_log',
'qm_scrm_campaigncenter_luckydraw_extra_chance',
'qm_scrm_campaigncenter_luckydraw_log',
'qm_scrm_campaign_survey_log',
'qm_scrm_campaigncenter_meeting_participant',
'qm_scrm_member',
'qm_scrm_member_info_log',
'qm_scrm_static_group_user',
'qm_scrm_member_address',
'qm_scrm_membership_discount',
'qm_scrm_red_package_log',
'qm_scrm_ec_order',
'qm_scrm_ec_order_refund',
'qm_scrm_trade',
'qm_scrm_trade_refund',
'qm_scrm_ec_promoter',
'qm_scrm_eccampaign_period_buy_order',
'qm_scrm_eccampaign_bargain_record',
'qm_scrm_eccampaign_bargain_help_record',
'qm_scrm_eccampaign_trial_record',
]
a_set = set(s1)
b_set = set(s2)
a_alone = b_set - a_set
print(a_alone)
