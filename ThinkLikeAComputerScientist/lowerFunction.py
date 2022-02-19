import re

if __name__ == '__main__':
    """使用正则表达式，将大写字母替换为_加小写字母"""
    s = [
        'id                      ',
        'startTime               ',
        'endTime                 ',
        'sType                   ',
        'treatedTime             ',
        'category                ',
        'categoryDetail          ',
        'evaluation              ',
        'evaluationType          ',
        'evaluationRemark        ',
        'staffInvitedEvaluateTime',
        'userJoinEvaluateTime    ',
        'relatedType             ',
        'relatedId               ',
        'interaction             ',
        'closeReason             ',
        'fromGroup               ',
        'fromGroupId             ',
        'fromStaff               ',
        'inQueueTime             ',
        'visitRange              ',
        'vipLevel                ',
        'staffId                 ',
        'staffName               ',
        'userId                  ',
        'foreignId               ',
        'fromIp                  ',
        'fromPage                ',
        'fromTitle               ',
        'fromType                ',
        'customFiled             ',
        'description             ',
        'transferRgType          ',
        'fromHumanTransfer       ',
        'transferFromStaffName   ',
        'transferFromGroup       ',
        'transferRemarks         ',
        'humanTransferSessionId  ',
        'worksheetIds            ',
        'roundNumber             ',
        'status                  ',
        'userResolvedStatus      ',
        'firstReplyCost          ',
        'avgRespDuration         ',
        'isValid                 ',
        'transferType            ',
        'staffMessageCount       ',
        'userMessageCount        ',
        'overflowFrom            ',
        'alarmTimes              ',
        'staffFirstReplyTime     ',
        'stickDuration           ',
        'clientFirstMessageTime  ',
        'isEvaluationInvited     ',
        'beginer                 ',
        'ender                   ',
        'originPlatform          ',
        'searchKey               ',
        'landPage                '
    ]
    for i in range(0,len(s)):
        sub = re.sub("[A-Z]", lambda x: "_" + x.group(0).lower(), s[i])
        print(sub)