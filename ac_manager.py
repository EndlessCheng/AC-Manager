# -*- coding: UTF-8 -*-
import urllib2


def get_html_with_user_agent(url):
    user_agent = "Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)"
    headers = {'User-Agent': user_agent}
    request = urllib2.Request(url, headers=headers)
    try:
        response = urllib2.urlopen(request)
    except urllib2.HTTPError, err:
        # if err.code == 404:
        raise
    html = response.read()
    return html


def get_ac_num(url, start_label, end_label="<", loop=1, add=0):
    try:
        html = get_html_with_user_agent(url)
    except urllib2.HTTPError, err:
        if err.code == 404:
            print "\t0"
            return 0
        else:
            raise

    start_position = 0
    for i in xrange(loop):
        start_position = html.find(start_label, start_position)
        if start_position == -1:  # not found this user or page error
            print "\t0"
            return 0
        start_position += len(start_label)
    start_position += add

    end_position = html.find(end_label, start_position)
    ac_num = int(html[start_position:end_position])
    print "\t%d" % ac_num
    return ac_num


def get_poj_ac_num():
    username = raw_input(u"POJ 用户名：".encode("GBK"))
    return get_ac_num(
        url="http://poj.org/userstatus?user_id=" + username,
        start_label="<a href=status?result=0&user_id=" + username + ">")


def get_hdu_ac_num():
    username = raw_input(u"HDU 用户名：".encode("GBK"))
    return get_ac_num(
        url="http://acm.hdu.edu.cn/userstatus.php?user=" + username,
        start_label="Problems Solved</td><td align=center>")


def get_zoj_ac_num():
    username = raw_input(u"ZOJ User ID（User Status 页面 URL 最后的那个数字）：".encode("GBK"))
    return get_ac_num(
        url="http://acm.zju.edu.cn/onlinejudge/showUserStatus.do?userId=" + username,
        start_label="AC Ratio:</font> <font color=\"red\" size=\"4\">",
        end_label="/")


def get_fzu_ac_num():
    username = raw_input(u"FZU 用户名：".encode("GBK"))
    return get_ac_num(
        url="http://acm.fzu.edu.cn/user.php?uname=" + username,
        start_label="Total Accepted</td>",
        add=7)


def get_sgu_ac_num():
    username = raw_input(u"SGU User ID：".encode("GBK"))
    return get_ac_num(
        url="http://acm.sgu.ru/teaminfo.php?id=" + username,
        start_label="Accepted: ")


def get_spoj_ac_num():
    username = raw_input(u"SPOJ 用户名：".encode("GBK"))
    return get_ac_num(
        url="http://www.spoj.com/users/" + username + "/",
        start_label="<td><b>")


def get_tju_ac_num():
    username = raw_input(u"TJU 用户名：".encode("GBK"))
    return get_ac_num(
        url="http://acm.tju.edu.cn/toj/user_" + username + ".html",
        start_label="Total Solved:</font> ",
        end_label="&")


def get_hnu_ac_num():
    username = raw_input(u"HNU 用户名：".encode("GBK"))
    return get_ac_num(
        url="http://acm.hnu.cn/online/?action=user&type=status&id=" + username,
        start_label="Accepts : <a href=\"./?action=status&userid=" + username + "&judgeresult=0\">")


def get_acdream_ac_num():
    username = raw_input(u"ACdream 用户名：".encode("GBK"))
    return get_ac_num(
        url="http://acdream.info/user/" + username,
        start_label="Solved: <span class=\"user user-green\">")


def get_uva_ac_num():
    username = raw_input(u"UVa User ID（uHunt URL 最后的那个数字）：".encode("GBK"))
    return get_ac_num(
        url="http://uva.onlinejudge.org/index.php?option=onlinejudge&page=show_authorstats&userid=" + username,
        start_label="<td width=\"20%\" align=\"center\"><h1 style=\"margin-top:-20px;margin-bottom:-5px;\">",
        loop=3)


def get_uvalive_ac_num():
    username = raw_input(u"UVALive User ID（获取方法见 http://www.ahmed-aly.com/HowToGetLAUserID.jsp）：".encode("GBK"))
    return get_ac_num(
        url="https://icpcarchive.ecs.baylor.edu/index.php?option=onlinejudge&page=show_authorstats&userid=" + username,
        start_label="<td width=\"20%\" align=\"center\"><h1 style=\"margin-top:-20px;margin-bottom:-5px;\">",
        loop=3)


def main():
    ac_cnt = 0
    ac_cnt += get_poj_ac_num()  # notice we have printed the AC number in get_ac_num()
    ac_cnt += get_hdu_ac_num()
    ac_cnt += get_zoj_ac_num()
    ac_cnt += get_fzu_ac_num()
    ac_cnt += get_sgu_ac_num()
    ac_cnt += get_spoj_ac_num()
    ac_cnt += get_tju_ac_num()
    ac_cnt += get_hnu_ac_num()
    ac_cnt += get_acdream_ac_num()
    ac_cnt += get_uva_ac_num()
    ac_cnt += get_uvalive_ac_num()
    print u"总 AC 数：%d".encode("GBK") % ac_cnt
    n = raw_input(u"按回车退出".encode("GBK"))


if __name__ == '__main__':
    main()

