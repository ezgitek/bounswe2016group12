package bounswe16group12.com.meanco;

import com.google.android.gms.analytics.GoogleAnalytics;
import com.google.android.gms.analytics.Tracker;
import android.app.Application;

import java.util.List;

import bounswe16group12.com.meanco.objects.Topic;
import bounswe16group12.com.meanco.tasks.GetTopicList;

/**
 * Created by Ezgi on 12/2/2016.
 */

public class MeancoApplication extends Application {

    private Tracker mTracker;
    public static final String SITE_URL = "http://46.101.253.73:8000/API/T/";
    public static final String POST_TAG_URL = "http://46.101.253.73:8000/API/AddTag";
    public static final String POST_TOPIC_URL = "http://46.101.253.73:8000/API/AddTopic/";
    public static final String POST_COMMENT_URL = "http://46.101.253.73:8000/API/AddComment/";
    public static final String POST_RELATION_URL = "http://46.101.253.73:8000/API/AddRelation/";
    public static final String WIKIDATA_URL = "https://www.wikidata.org/w/api.php?action=wbsearchentities&language=en&format=json&search=";
    public static final String SEARCH_URL = "http://46.101.253.73:8000/API/SearchTopic?search=";
    public static final String REGISTER_URL = "http://46.101.253.73:8000/API/Register";
    public static final String LOGIN_URL = "http://46.101.253.73:8000/API/Login";
    public static final String VOTE_COMMENT_URL = "http://46.101.253.73:8000/API/RateComment";
    private static final String GOOGLE_ANALYTICS_KEY = "UA-39760660-5";

    public MeancoApplication() {
        // this method fires only once per application start.
        // getApplicationContext returns null here

    }

    /**
     * Gets the default {@link Tracker} for this {@link Application}.
     * @return tracker
     */
    synchronized public Tracker getDefaultTracker() {
        if (mTracker == null) {
            GoogleAnalytics analytics = GoogleAnalytics.getInstance(this);
            // To enable debug logging use: adb shell setprop log.tag.GAv4 DEBUG
            mTracker = analytics.newTracker(GOOGLE_ANALYTICS_KEY);
        }
        return mTracker;
    }

}