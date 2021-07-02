This is a really simple program I made when confronted by unix time for the first time.

Context: 

Unix time is a measurement of time from what is referred to as the Unix epoch (00:00:00 UTC on 1 January 1970), minus leap seconds.
See this link for more details: https://en.wikipedia.org/wiki/Unix_time  
For example, Friday, 2 July 2021 16:20:13 GMT+01:00 is actually 1625239213000 milliseconds in UNIX time.

I encountered this when using the AWS CLI when investigating some log streams (https://docs.aws.amazon.com/cli/latest/reference/logs/describe-log-streams.html).  As many of the timesatmps are in Unix time I had to find a way to convert *many* of these to a more human-freindly format for a infrastructure report.

I had also just begun learning Python, staring this excellent free course to target the PCEP exam: https://edube.org/study/pe1

This was an excellent opportunity to have some fun and practise, so I created a stand-alond converter to build a component of the larger script planned.


Feel free to use, and I hope you enjoy!