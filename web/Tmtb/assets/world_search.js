var n = {};
n.api = "mtop.user.getUserSimple";
n.data = "{}";
n.dataType = "jsonp";
n.ecode = 1;
n.jsonpIncPrefix = "liblogin";
n.sessionOption = "AutoLoginOnly";
n.type = "get";
n.v = "1.0";


var r = {};
r.H5Request = true;
r.mainDomain = "taobao.com";
r.getJSONP = true;
r.prefix = "h5api";
r.safariGoLogin = true;
r.subDomain = "m";
r.token = "26b24ad313c4a44bb3216612f79dc36d";   // _m_h5_c  | _m_h5_tk



function t(e, t) {
	return e << t | e >>> 32 - t
}





function structure( e ) {

	function i(e, r, i, o, a, c, s) {
		return e = n(e, n(n(function(e, t, n) {
			return e & n | t & ~n
		}(r, i, o), a), s)),
		n(t(e, c), r)
	}

	function o(e, r, i, o, a, c, s) {
		return e = n(e, n(n(function(e, t, n) {
			return e ^ t ^ n
		}(r, i, o), a), s)),
		n(t(e, c), r)
	}

	function a(e, r, i, o, a, c, s) {
		return e = n(e, n(n(function(e, t, n) {
			return t ^ (e | ~n)
		}(r, i, o), a), s)),
		n(t(e, c), r)
	}

	function c(e) {
		var t, n = "", r = "";
		for (t = 0; 3 >= t; t++)
			n += (r = "0" + (e >>> 8 * t & 255).toString(16)).substr(r.length - 2, 2);
		return n
	}


	function r(e, r, i, o, a, c, s) {
		return e = n(e, n(n(function(e, t, n) {
			return e & t | ~e & n
		}(r, i, o), a), s)),
		n(t(e, c), r)
	}

	function n(e, t) {
		var n, r, i, o, a;
		return i = 2147483648 & e,
		o = 2147483648 & t,
		a = (1073741823 & e) + (1073741823 & t),
		(n = 1073741824 & e) & (r = 1073741824 & t) ? 2147483648 ^ a ^ i ^ o : n | r ? 1073741824 & a ? 3221225472 ^ a ^ i ^ o : 1073741824 ^ a ^ i ^ o : a ^ i ^ o
	}

	var s, u, l, f, p, d, h, m, v, g;
	for (g = function(e) {
		for (var t, n = e.length, r = n + 8, i = 16 * ((r - r % 64) / 64 + 1), o = new Array(i - 1), a = 0, c = 0; n > c; )
			a = c % 4 * 8,
			o[t = (c - c % 4) / 4] = o[t] | e.charCodeAt(c) << a,
			c++;
		return a = c % 4 * 8,
		o[t = (c - c % 4) / 4] = o[t] | 128 << a,
		o[i - 2] = n << 3,
		o[i - 1] = n >>> 29,
		o
	}(e = function(e) {
		e = e.replace(/\r\n/g, "\n");
		for (var t = "", n = 0; n < e.length; n++) {
			var r = e.charCodeAt(n);
			128 > r ? t += String.fromCharCode(r) : r > 127 && 2048 > r ? (t += String.fromCharCode(r >> 6 | 192),
			t += String.fromCharCode(63 & r | 128)) : (t += String.fromCharCode(r >> 12 | 224),
			t += String.fromCharCode(r >> 6 & 63 | 128),
			t += String.fromCharCode(63 & r | 128))
		}
		return t
	}(e)),
	d = 1732584193,
	h = 4023233417,
	m = 2562383102,
	v = 271733878,
	s = 0; s < g.length; s += 16)
		u = d,
		l = h,
		f = m,
		p = v,
		d = r(d, h, m, v, g[s + 0], 7, 3614090360),
		v = r(v, d, h, m, g[s + 1], 12, 3905402710),
		m = r(m, v, d, h, g[s + 2], 17, 606105819),
		h = r(h, m, v, d, g[s + 3], 22, 3250441966),
		d = r(d, h, m, v, g[s + 4], 7, 4118548399),
		v = r(v, d, h, m, g[s + 5], 12, 1200080426),
		m = r(m, v, d, h, g[s + 6], 17, 2821735955),
		h = r(h, m, v, d, g[s + 7], 22, 4249261313),
		d = r(d, h, m, v, g[s + 8], 7, 1770035416),
		v = r(v, d, h, m, g[s + 9], 12, 2336552879),
		m = r(m, v, d, h, g[s + 10], 17, 4294925233),
		h = r(h, m, v, d, g[s + 11], 22, 2304563134),
		d = r(d, h, m, v, g[s + 12], 7, 1804603682),
		v = r(v, d, h, m, g[s + 13], 12, 4254626195),
		m = r(m, v, d, h, g[s + 14], 17, 2792965006),
		d = i(d, h = r(h, m, v, d, g[s + 15], 22, 1236535329), m, v, g[s + 1], 5, 4129170786),
		v = i(v, d, h, m, g[s + 6], 9, 3225465664),
		m = i(m, v, d, h, g[s + 11], 14, 643717713),
		h = i(h, m, v, d, g[s + 0], 20, 3921069994),
		d = i(d, h, m, v, g[s + 5], 5, 3593408605),
		v = i(v, d, h, m, g[s + 10], 9, 38016083),
		m = i(m, v, d, h, g[s + 15], 14, 3634488961),
		h = i(h, m, v, d, g[s + 4], 20, 3889429448),
		d = i(d, h, m, v, g[s + 9], 5, 568446438),
		v = i(v, d, h, m, g[s + 14], 9, 3275163606),
		m = i(m, v, d, h, g[s + 3], 14, 4107603335),
		h = i(h, m, v, d, g[s + 8], 20, 1163531501),
		d = i(d, h, m, v, g[s + 13], 5, 2850285829),
		v = i(v, d, h, m, g[s + 2], 9, 4243563512),
		m = i(m, v, d, h, g[s + 7], 14, 1735328473),
		d = o(d, h = i(h, m, v, d, g[s + 12], 20, 2368359562), m, v, g[s + 5], 4, 4294588738),
		v = o(v, d, h, m, g[s + 8], 11, 2272392833),
		m = o(m, v, d, h, g[s + 11], 16, 1839030562),
		h = o(h, m, v, d, g[s + 14], 23, 4259657740),
		d = o(d, h, m, v, g[s + 1], 4, 2763975236),
		v = o(v, d, h, m, g[s + 4], 11, 1272893353),
		m = o(m, v, d, h, g[s + 7], 16, 4139469664),
		h = o(h, m, v, d, g[s + 10], 23, 3200236656),
		d = o(d, h, m, v, g[s + 13], 4, 681279174),
		v = o(v, d, h, m, g[s + 0], 11, 3936430074),
		m = o(m, v, d, h, g[s + 3], 16, 3572445317),
		h = o(h, m, v, d, g[s + 6], 23, 76029189),
		d = o(d, h, m, v, g[s + 9], 4, 3654602809),
		v = o(v, d, h, m, g[s + 12], 11, 3873151461),
		m = o(m, v, d, h, g[s + 15], 16, 530742520),
		d = a(d, h = o(h, m, v, d, g[s + 2], 23, 3299628645), m, v, g[s + 0], 6, 4096336452),
		v = a(v, d, h, m, g[s + 7], 10, 1126891415),
		m = a(m, v, d, h, g[s + 14], 15, 2878612391),
		h = a(h, m, v, d, g[s + 5], 21, 4237533241),
		d = a(d, h, m, v, g[s + 12], 6, 1700485571),
		v = a(v, d, h, m, g[s + 3], 10, 2399980690),
		m = a(m, v, d, h, g[s + 10], 15, 4293915773),
		h = a(h, m, v, d, g[s + 1], 21, 2240044497),
		d = a(d, h, m, v, g[s + 8], 6, 1873313359),
		v = a(v, d, h, m, g[s + 15], 10, 4264355552),
		m = a(m, v, d, h, g[s + 6], 15, 2734768916),
		h = a(h, m, v, d, g[s + 13], 21, 1309151649),
		d = a(d, h, m, v, g[s + 4], 6, 4149444226),
		v = a(v, d, h, m, g[s + 11], 10, 3174756917),
		m = a(m, v, d, h, g[s + 2], 15, 718787259),
		h = a(h, m, v, d, g[s + 9], 21, 3951481745),
		d = n(d, u),
		h = n(h, l),
		m = n(m, f),
		v = n(v, p);
	return (c(d) + c(h) + c(m) + c(v)).toLowerCase()
}

c = 12574478;

function getSign( token, t, data ) {
	s = t;
	u = structure( token + "&" + s + "&" + c + "&" + data );

	return u;
}
